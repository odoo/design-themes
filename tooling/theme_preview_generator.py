"""Generate static configurator preview HTML files for design themes.

The website configurator needs theme previews before a theme is installed, so it
cannot rely on pages, attachments, or assets created only during theme
application. This script starts a temporary Odoo database, applies each theme
through the website configurator, downloads the generated homepage, and rewrites
it into a self-contained ``static/description/preview.html`` suitable for those
pre-installation previews.
"""

import json
import re
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


REPOS_DIR = Path(__file__).resolve().parents[2]
ODOO_DIR = REPOS_DIR / "odoo"
THEMES_DIR = REPOS_DIR / "design-themes"
ODOO_BIN = ODOO_DIR / "odoo-bin"
DATABASE = "generate-html"
BASE_URL = "http://localhost:8888"
LOGIN = "admin"
PASSWORD = "admin"
EXCLUDED_THEMES = {"test_theme", "test_themes", "theme_common"}

# Edit these directly if you want to change how Odoo starts.
ODOO_ARGS = [
    "--http-interface=localhost",
    "--http-port=8888",
    f"--addons-path={ODOO_DIR / 'addons'},{THEMES_DIR}",
    f"--database={DATABASE}",
    "--init=website",
]

# Edit these directly if you want different configurator values.
CONFIGURATOR_VALUES = {
    "industry_id": 0,
    "industry_name": "business",
    "selected_features": [],
    "selected_palette": "base-1",
    "website_purpose": "general",
    "website_type": "business",
    "skip_ai": True,
}

DOWNLOAD_SESSION = requests.Session()
DOWNLOAD_SESSION.headers["User-Agent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
PSEUDO_RE = re.compile(r'::?[a-zA-Z-]+(\([^)]*\))?')
CSS_URL_RE = re.compile(
    r'url\(\s*'
    r'(?:"([^"]*)"|\'([^\']*)\'|([^)]*))'
    r'\s*\)'
)
VH_RE = re.compile(r"(-?(?:\d+(?:\.\d+)?|\.\d+))s?vh")
PALETTE_COLORS = {
    "--o-color-1": ("#714B67",),
    "--o-color-2": ("#F0CDA8",),
    "--o-color-3": ("#F6F5F4",),
    "--o-color-4": ("#FFFFFF", "#FFF"),
    "--o-color-5": ("#1B1319",),
}
FONT_MIME_TYPES = {
    ".woff2": "font/woff2",
    ".woff": "font/woff",
    ".ttf": "font/ttf",
    ".otf": "font/otf",
    ".eot": "application/vnd.ms-fontobject",
}
FONT_ASSET_URLS = {
    "web.fontawesome.min.woff2": "/web/static/src/libs/fontawesome/fonts/fontawesome-webfont.woff2",
    "web.fontawesome.min.woff": "/web/static/src/libs/fontawesome/fonts/fontawesome-webfont.woff",
    "web.odoo_ui_icons.min.woff2": "/web/static/lib/odoo_ui_icons/fonts/odoo_ui_icons.woff2",
    "web.odoo_ui_icons.min.woff": "/web/static/lib/odoo_ui_icons/fonts/odoo_ui_icons.woff",
}
COLOR_TOKEN_END = r"(?![0-9a-zA-Z_-])"
VH_TO_VW_RATIO = 10 / 16


def get_theme_dirs():
    theme_dirs = []
    for path in sorted(THEMES_DIR.iterdir()):
        if not path.is_dir():
            continue
        if path.name in EXCLUDED_THEMES:
            continue
        if not path.name.startswith("theme_"):
            continue
        if not (path / "__manifest__.py").exists():
            continue
        theme_dirs.append(path)
    return theme_dirs


def get_preview_output_path(theme_dir):
    description_dir = theme_dir / "static" / "description"
    svg_paths = sorted(description_dir.glob("*.svg"))
    if svg_paths:
        return svg_paths[0].with_name("preview.html")
    return description_dir / "preview.html"


def start_odoo():
    subprocess.run(["dropdb", "--if-exists", DATABASE], check=True, cwd=ODOO_BIN.parent)
    command = [sys.executable, str(ODOO_BIN), *ODOO_ARGS]
    return subprocess.Popen(command, cwd=ODOO_BIN.parent)


def stop_odoo(server):
    if server.poll() is not None:
        return
    server.terminate()
    try:
        server.wait(timeout=30)
    except subprocess.TimeoutExpired:
        server.kill()
        server.wait()


def wait_for_odoo(server):
    deadline = time.time() + 180
    while time.time() < deadline:
        if server.poll() is not None:
            raise RuntimeError("Odoo stopped before it was ready.")
        try:
            response = requests.get(f"{BASE_URL}/web/login", timeout=5)
            if response.ok:
                return
        except requests.RequestException:
            pass
        time.sleep(1)
    raise RuntimeError("Odoo did not start in time.")


def jsonrpc(session, url, params, timeout=30):
    response = session.post(
        url,
        json={
            "jsonrpc": "2.0",
            "method": "call",
            "params": params,
            "id": 1,
        },
        timeout=timeout,
    )
    response.raise_for_status()
    payload = response.json()
    if payload.get("error"):
        raise RuntimeError(json.dumps(payload["error"], indent=2))
    return payload["result"]


def login(session):
    session_info = jsonrpc(
        session,
        f"{BASE_URL}/web/session/authenticate",
        {
            "db": DATABASE,
            "login": LOGIN,
            "password": PASSWORD,
        },
    )
    if not session_info.get("uid"):
        raise RuntimeError("Login failed.")
    return session_info


def generate_website(session, context, theme_name):
    return jsonrpc(
        session,
        f"{BASE_URL}/web/dataset/call_kw/website/configurator_apply",
        {
            "model": "website",
            "method": "configurator_apply",
            "args": [],
            "kwargs": {
                **CONFIGURATOR_VALUES,
                "theme_name": theme_name,
                "context": context,
            },
        },
        timeout=600,
    )


def fetch(url):
    try:
        response = DOWNLOAD_SESSION.get(url, timeout=30)
        response.raise_for_status()
        return response.content, response.headers.get("Content-Type", "")
    except Exception as error:
        print(f"  WARN: {url} - {error}", file=sys.stderr)
        return None, None


def root_relative_url(url, base_url):
    if not url or url.startswith(("data:", "#")):
        return url
    parsed = urlparse(urljoin(base_url, url))
    path = parsed.path or "/"
    if parsed.query:
        path += f"?{parsed.query}"
    if parsed.fragment:
        path += f"#{parsed.fragment}"
    return path


def is_external_url(url, base_url):
    parsed = urlparse(urljoin(base_url, url))
    base = urlparse(base_url)
    return bool(parsed.netloc and parsed.netloc != base.netloc)


def get_font_mime_type(url):
    suffix = Path(urlparse(url).path).suffix.lower()
    return FONT_MIME_TYPES.get(suffix)

def resolve_css_imports(css, base_url):
    def replace(match):
        url = match.group(1) or match.group(2)
        if not url:
            return ""
        raw, _ = fetch(urljoin(base_url, url))
        if not raw:
            return ""
        return resolve_css_imports(raw.decode("utf-8", errors="replace"), urljoin(base_url, url))

    return re.sub(
        r'@import\s+(?:url\(["\']?([^)"\']+)["\']?\)|["\']([^"\']+)["\'])\s*;',
        replace,
        css,
    )


def resolve_css_urls(css, base_url):
    def replace(match):
        raw_url, _quote = get_css_url(match)
        if raw_url.startswith("data:"):
            return match.group(0)
        font_asset_url = get_stable_font_asset_url(raw_url)
        if font_asset_url:
            return f'url("{font_asset_url}")'
        if get_font_mime_type(raw_url):
            if is_external_url(raw_url, base_url):
                return f'url("{urljoin(base_url, raw_url)}")'
            return f'url("{root_relative_url(raw_url, base_url)}")'
        return f'url("{root_relative_url(raw_url, base_url)}")'

    return CSS_URL_RE.sub(replace, css)


def get_stable_font_asset_url(url):
    filename = Path(urlparse(url).path).name
    return FONT_ASSET_URLS.get(filename)


def get_css_url(match):
    double_quoted_url, single_quoted_url, unquoted_url = match.groups()
    if double_quoted_url is not None:
        return double_quoted_url, '"'
    if single_quoted_url is not None:
        return single_quoted_url, "'"
    return unquoted_url.strip(), ""


def replace_color_token(text, color, replacement):
    # Do not replace #FFF inside #FFF3CD or %23FFF inside %23FFF3CD.
    return re.sub(
        rf"{re.escape(color)}{COLOR_TOKEN_END}",
        replacement,
        text,
        flags=re.I,
    )


def replace_palette_colors_in_css(css_text):
    protected = {}
    for css_var, colors in PALETTE_COLORS.items():
        for color in colors:
            placeholder = f"__KEEP_{css_var.strip('-').replace('-', '_')}_{len(protected)}__"
            pattern = re.compile(
                rf"({re.escape(css_var)}\s*:\s*)"
                rf"{re.escape(color)}{COLOR_TOKEN_END}",
                re.I,
            )
            css_text = pattern.sub(lambda match: f"{match.group(1)}{placeholder}", css_text)
            protected[placeholder] = color

    for css_var, colors in PALETTE_COLORS.items():
        for color in colors:
            css_text = replace_color_token(css_text, color, f"var({css_var})")

    for placeholder, color in protected.items():
        css_text = css_text.replace(placeholder, color)
    return css_text


def replace_palette_colors_in_url(url):
    for css_var, colors in PALETTE_COLORS.items():
        color_token = css_var.removeprefix("--")
        for color in colors:
            encoded_color = "%23" + color.lstrip("#")
            url = replace_color_token(url, encoded_color, color_token)
    return url


def replace_palette_colors_in_urls(text):
    def replace(match):
        raw_url, quote = get_css_url(match)
        if raw_url.startswith("data:"):
            # Inline SVG icons need real colors, not palette tokens.
            return match.group(0)
        url = replace_palette_colors_in_url(raw_url)
        return f"url({quote}{url}{quote})"

    return CSS_URL_RE.sub(replace, text)


def replace_palette_colors_in_style(style_text):
    style_text = replace_palette_colors_in_urls(style_text)
    for css_var, colors in PALETTE_COLORS.items():
        for color in colors:
            style_text = replace_color_token(style_text, color, f"var({css_var})")
    return style_text


def replace_palette_colors_in_attributes(soup):
    for tag in soup.find_all(True):
        for attribute in ("fill", "stroke", "stop-color", "color"):
            value = tag.get(attribute)
            if not value:
                continue
            tag[attribute] = replace_palette_colors_in_style(value)


def inject_palette_variables(soup):
    if soup.head is None:
        soup.html.insert(0, soup.new_tag("head"))
    style = soup.new_tag("style")
    style["id"] = "preview-palette-vars"
    style.string = ":root{" + " ".join(
        f"{css_var}: {colors[0]};" for css_var, colors in PALETTE_COLORS.items()
    ) + "}"
    soup.head.append(style)


def inject_color_combination_text_overrides(soup):
    if soup.head is None:
        soup.html.insert(0, soup.new_tag("head"))

    heading_selectors = "h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6"
    rules = []
    for index in range(1, 6):
        text_color = f"var(--o-cc{index}-text)"
        rules.append(f".o_cc{index}{{--color:{text_color};color:{text_color};}}")
        rules.append(
            f".o_cc{index} :is({heading_selectors}),"
            f".o_colored_level .o_cc{index} :is({heading_selectors})"
            f"{{color:{text_color};}}"
        )

    style = soup.new_tag("style")
    style["id"] = "preview-color-combination-text-overrides"
    style.string = "".join(rules)
    soup.head.append(style)


def convert_vh_to_vw(css_text, ratio=VH_TO_VW_RATIO):
    if "vh" not in css_text:
        return css_text

    def replace(match):
        vw = float(match.group(1)) * ratio
        return f"{vw:g}vw"

    return VH_RE.sub(replace, css_text)


def remove_parallax_fixed_background(css_text):
    def replace(match):
        selector = match.group(1)
        body = match.group(2)
        if ".s_parallax_bg" not in selector:
            return match.group(0)
        body = re.sub(r"\s*background-attachment\s*:\s*fixed\s*;?", "", body, flags=re.I)
        return f"{selector}{{{body}}}"

    return re.sub(r"([^{}]+)\{([^{}]*)\}", replace, css_text)


def process_css(css_text, base_url):
    css_text = resolve_css_imports(css_text, base_url)
    css_text = resolve_css_urls(css_text, base_url)
    css_text = convert_vh_to_vw(css_text)
    css_text = remove_parallax_fixed_background(css_text)
    css_text = replace_palette_colors_in_urls(css_text)
    return replace_palette_colors_in_css(css_text)


def inline_stylesheets(soup, base_url):
    for link in soup.find_all("link", rel=lambda rel: rel and "stylesheet" in rel):
        href = link.get("href")
        if not href:
            link.decompose()
            continue
        abs_url = urljoin(base_url, href)
        raw, _ = fetch(abs_url)
        if not raw:
            link.decompose()
            continue
        style = soup.new_tag("style")
        style.string = process_css(raw.decode("utf-8", errors="replace"), abs_url)
        link.replace_with(style)


def inline_style_blocks(soup, base_url):
    for style in soup.find_all("style"):
        if style.string:
            style.string = process_css(style.string, base_url)


def inline_inline_styles(soup, base_url):
    for tag in soup.find_all(style=True):
        style = resolve_css_urls(tag["style"], base_url)
        style = convert_vh_to_vw(style)
        tag["style"] = replace_palette_colors_in_style(style)


def inline_images(soup, base_url):
    for image in soup.find_all("img"):
        src = image.get("src", "")
        if src:
            image["src"] = root_relative_url(src, base_url)
        image.attrs.pop("srcset", None)

    for source in soup.find_all("source"):
        source.attrs.pop("srcset", None)


def inline_favicons(soup, base_url):
    for link in soup.find_all("link", rel=lambda rel: rel and ("icon" in rel or "apple-touch-icon" in rel)):
        href = link.get("href")
        if href:
            link["href"] = root_relative_url(href, base_url)


def inline_font_preloads(soup, base_url):
    for link in soup.find_all("link", attrs={"as": "font"}):
        href = link.get("href")
        if not href:
            continue
        font_asset_url = get_stable_font_asset_url(href)
        if font_asset_url:
            link["href"] = font_asset_url
            continue
        if is_external_url(href, base_url):
            link["href"] = urljoin(base_url, href)
            continue
        link["href"] = root_relative_url(href, base_url)


def remove_preview_metadata(soup):
    for tag in soup.find_all("meta", property=lambda value: value in ("og:url", "og:image")):
        tag.decompose()
    for tag in soup.find_all("meta", attrs={"name": "twitter:image"}):
        tag.decompose()

    for link in soup.find_all("link"):
        rel = link.get("rel", [])
        rel = [rel] if isinstance(rel, str) else rel
        rel = {value.lower() for value in rel}
        if rel & {"canonical", "apple-touch-icon", "icon"}:
            link.decompose()


def remove_javascript(soup):
    for script in soup.find_all("script"):
        script.decompose()

    for noscript in soup.find_all("noscript"):
        noscript.unwrap()

    for tag in soup.find_all(True):
        for attribute in list(tag.attrs):
            if attribute.lower().startswith("on"):
                del tag[attribute]

    for link in soup.find_all("a", href=re.compile(r"^\s*javascript:", re.I)):
        link["href"] = "#"


def remove_animation_classes(soup):
    for tag in soup.select(".o_animate"):
        classes = [class_name for class_name in tag.get("class", []) if class_name != "o_animate"]
        if classes:
            tag["class"] = classes
        else:
            tag.attrs.pop("class", None)


def fix_floating_blocks_preview(soup):
    # counter s_floating_blocks opacity:0 on each block plus some CSS magic to
    # reproduce the overlapping stack effect without requiring JS.
    if not soup.select_one(".s_floating_blocks"):
        return
    style = soup.new_tag("style")
    style["id"] = "preview-floating-blocks"
    style.string = (
        ".s_floating_blocks .s_floating_blocks_block"
        "{opacity:1!important;position:relative!important}"
        ".s_floating_blocks .s_floating_blocks_block:nth-child(1)"
        "{z-index:1;transform:scale(.96)!important}"
        ".s_floating_blocks .s_floating_blocks_block:nth-child(2)"
        "{z-index:2;transform:scale(.98)!important;margin-top:-45%!important}"
        ".s_floating_blocks .s_floating_blocks_block:nth-child(3)"
        "{z-index:3;margin-top:-45%!important}"
    )
    soup.head.append(style)


def _skip_string(css, position):
    quote = css[position]
    position += 1
    while position < len(css):
        if css[position] == "\\":
            position += 2
            continue
        if css[position] == quote:
            return position + 1
        position += 1
    return position


def _skip_comment(css, position):
    end = css.find("*/", position + 2)
    return end + 2 if end != -1 else len(css)


def _find_block_end(css, start):
    depth = 1
    position = start + 1
    while position < len(css) and depth > 0:
        char = css[position]
        if char in ('"', "'"):
            position = _skip_string(css, position)
        elif char == "/" and position + 1 < len(css) and css[position + 1] == "*":
            position = _skip_comment(css, position)
        elif char == "{":
            depth += 1
            position += 1
        elif char == "}":
            depth -= 1
            position += 1
        else:
            position += 1
    return position


def _selector_is_used(soup, selector_text):
    for part in selector_text.split(","):
        cleaned = PSEUDO_RE.sub("", part).strip()
        if not cleaned:
            return True
        try:
            if soup.select_one(cleaned):
                return True
        except Exception:
            return True
    return False


def _purge_css_text(css, soup):
    result = []
    position = 0
    while position < len(css):
        whitespace_start = position
        while position < len(css) and css[position] in " \t\n\r\f":
            position += 1
        if position >= len(css):
            result.append(css[whitespace_start:position])
            break

        if css[position:position + 2] == "/*":
            end = _skip_comment(css, position)
            result.append(css[whitespace_start:end])
            position = end
            continue

        if css[position] == "@":
            at_start = position
            position += 1
            while position < len(css) and (css[position].isalpha() or css[position] == "-"):
                position += 1
            keyword = css[at_start + 1:position].strip().lower()
            if keyword in ("import", "charset", "namespace"):
                end = css.find(";", position)
                if end == -1:
                    result.append(css[whitespace_start:])
                    break
                result.append(css[whitespace_start:end + 1])
                position = end + 1
            else:
                brace = css.find("{", position)
                if brace == -1:
                    result.append(css[whitespace_start:])
                    break
                end = _find_block_end(css, brace)
                result.append(css[whitespace_start:end])
                position = end
            continue

        brace = css.find("{", position)
        if brace == -1:
            result.append(css[whitespace_start:])
            break

        selector = css[position:brace].strip()
        end = _find_block_end(css, brace)
        rule_text = css[whitespace_start:end]
        if not selector or _selector_is_used(soup, selector):
            result.append(rule_text)
        position = end

    return "".join(result)


def purge_unused_css(soup):
    for style in soup.find_all("style"):
        if not style.string:
            continue
        cleaned = _purge_css_text(style.string, soup)
        if cleaned.strip():
            style.string = cleaned
        else:
            style.decompose()


def download_static_html(url, output_path):
    print(f"Downloading {url} -> {output_path}")
    raw, _ = fetch(url)
    if not raw:
        raise RuntimeError("Could not download the generated website.")

    soup = BeautifulSoup(raw, "html.parser")
    inline_stylesheets(soup, url)
    inline_style_blocks(soup, url)
    inline_inline_styles(soup, url)
    inline_images(soup, url)
    inline_favicons(soup, url)
    inline_font_preloads(soup, url)
    remove_preview_metadata(soup)
    replace_palette_colors_in_attributes(soup)
    remove_javascript(soup)
    remove_animation_classes(soup)
    purge_unused_css(soup)
    fix_floating_blocks_preview(soup)
    inject_palette_variables(soup)
    inject_color_combination_text_overrides(soup)

    for meta in soup.find_all("meta", attrs={"http-equiv": True}):
        if meta["http-equiv"].lower() in ("refresh", "content-security-policy"):
            meta.decompose()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(str(soup), encoding="utf-8")


def get_generated_page_url(result):
    path = "/"
    action = result.get("url")
    if isinstance(action, str):
        path = action
    elif isinstance(action, dict):
        path = action.get("params", {}).get("path") or "/"
    return urljoin(f"{BASE_URL}/", path)


def generate_theme_preview(theme_dir):
    theme_name = theme_dir.name
    output_path = get_preview_output_path(theme_dir)
    print(f"Generating {theme_name}")

    server = start_odoo()
    session = requests.Session()
    try:
        wait_for_odoo(server)
        session_info = login(session)
        result = generate_website(session, session_info.get("user_context", {}), theme_name)
        download_static_html(get_generated_page_url(result), output_path)
        print(f"Saved {output_path}")
    finally:
        session.close()
        stop_odoo(server)


def main():
    for theme_dir in get_theme_dirs():
        generate_theme_preview(theme_dir)


if __name__ == "__main__":
    main()
