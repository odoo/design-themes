"""Generate static configurator preview files for design themes.

The website configurator needs theme previews before a theme is installed, so it
cannot rely on pages, attachments, or assets created only during theme
application. This script starts a temporary Odoo database, applies each theme
through the website configurator, downloads the generated homepage, and rewrites
it into a self-contained ``static/description/preview.html`` (light variant)
suitable for those pre-installation previews.

The dark variant is not written as a full HTML page: its markup is derivable
from the light one (the website side runs ``adapt_dark_palette_content`` on
it), so only its CSS differs. ``static/description/preview_dark.css`` holds
the declarations that, appended after ``preview.html``'s CSS, reproduce the
dark homepage's cascade on that derived markup (see ``build_dark_css_diff``).
"""

import colorsys
import json
import os
import re
import subprocess
import sys
import time
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from itertools import groupby
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

REPOS_DIR = Path(__file__).resolve().parents[2]
ODOO_DIR = REPOS_DIR / "odoo"
THEMES_DIR = REPOS_DIR / "design-themes"
ODOO_BIN = ODOO_DIR / "odoo-bin"
LOGIN = "admin"
PASSWORD = "admin"
EXCLUDED_THEMES = {"test_theme", "test_themes", "theme_common"}

# Applying a theme reloads the whole registry, which is serialized within a
# database but parallel across instances: themes are sharded over workers, each
# with its own Odoo, port and template copy of a base database where
# ``website`` is installed once. Each worker costs ~1GB RAM.
BASE_DATABASE = "generate-html"
BASE_HTTP_PORT = 8888
NUM_WORKERS = int(os.environ.get("PREVIEW_WORKERS", min(4, os.cpu_count() or 1)))
BOOT_STAGGER_SECONDS = 3
STYLESHEET_FETCH_WORKERS = 6

ADDONS_PATH = f"{ODOO_DIR / 'addons'},{THEMES_DIR}"

# Reassigned per worker in ``run_worker``.
DATABASE = BASE_DATABASE
HTTP_PORT = BASE_HTTP_PORT
BASE_URL = f"http://localhost:{BASE_HTTP_PORT}"
# Host header pinning the anonymous download to the current theme's website.
PREVIEW_HOST = None

GENERIC_ODOO_ARGS = [
    f"--addons-path={ADDONS_PATH}",
    "--log-handler=:WARNING",
    "--max-cron-threads=0",
]


CONFIGURATOR_VALUES = {
    "industry_id": 0,
    "industry_name": "business",
    "selected_features": [],
    "website_purpose": "general",
    "website_type": "business",
    "skip_ai": True,
}

MENU_ITEMS = [("Shop", "/shop"), ("Event", "/event")]

DOWNLOAD_SESSION = requests.Session()
DOWNLOAD_SESSION.headers["User-Agent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
PSEUDO_RE = re.compile(r'::?[a-zA-Z-]+(\([^)]*\))?')
PSEUDO_ELEMENT_RE = re.compile(r'::?(before|after|first-line|first-letter|marker|selection|placeholder|backdrop|file-selector-button)\b')
CSS_URL_RE = re.compile(
    r'url\(\s*'
    r'(?:"([^"]*)"|\'([^\']*)\'|([^)]*))'
    r'\s*\)',
)
VH_RE = re.compile(r"(-?(?:\d+(?:\.\d+)?|\.\d+))s?vh")
LIGHT_PALETTE_COLORS = {
    "--o-color-1": ("#714B67",),
    "--o-color-2": ("#F0CDA8",),
    "--o-color-3": ("#F6F5F4",),
    "--o-color-4": ("#FFFFFF", "#FFF"),
    "--o-color-5": ("#1B1319",),
}
# default-dark-2: a saturated primary keeps its shades apart from the surfaces.
DARK_PALETTE_COLORS = {
    "--o-color-1": ("#A78BFA",),
    "--o-color-2": ("#E68CB5",),
    "--o-color-3": ("#251C40",),
    "--o-color-4": ("#1B142E",),
    "--o-color-5": ("#FFFFFF", "#FFF"),
}
PALETTE_COLORS = LIGHT_PALETTE_COLORS
PREVIEW_VARIANTS = (
    ("", LIGHT_PALETTE_COLORS, "base-1", False),
    ("-dark", DARK_PALETTE_COLORS, "default-dark-2", True),
)
FONT_ASSET_URLS = {
    "web.material_symbols_outlined.min.woff2": "/web/static/src/libs/materialsymbols/material_symbols_outlined_subset.woff2",
    "web.material_symbols_sharp.min.woff2": "/web/static/src/libs/materialsymbols/material_symbols_sharp_subset.woff2",
    "web.odoo_ui_icons.min.woff2": "/web/static/lib/odoo_ui_icons/fonts/odoo_ui_icons.woff2",
}
DEFAULT_WEBSITE_LOGO_URL = "/website/static/src/img/website_logo.svg"
WEBSITE_LOGO_URL_RE = re.compile(r"^/web/image/website/\d+/logo(?:[/?#].*)?$")
COLOR_TOKEN_END = r"(?![0-9a-zA-Z_-])"
PALETTE_RGB_RE = re.compile(
    r"(-rgb:\s*|rgba?\(\s*)([0-9.]+)\s*,\s*([0-9.]+)\s*,\s*([0-9.]+)",
)
DERIVED_COLOR_RE = re.compile(r"url\([^)]*\)|#[0-9a-fA-F]{6}(?![0-9a-zA-Z_-])")
VH_TO_VW_RATIO = 10 / 16


def elapsed(start):
    return f"{time.perf_counter() - start:.1f}s"


def get_theme_dirs():
    return [
        path for path in sorted(THEMES_DIR.iterdir())
        if path.is_dir()
        and path.name not in EXCLUDED_THEMES
        and path.name.startswith("theme_")
        and (path / "__manifest__.py").exists()
    ]


def get_preview_output_path(theme_dir, filename):
    description_dir = theme_dir / "static" / "description"
    svg_paths = sorted(description_dir.glob("*.svg"))
    if svg_paths:
        return svg_paths[0].with_name(filename)
    return description_dir / filename


def prepare_base_database():
    print(f"Preparing base database {BASE_DATABASE} (website install, once).")
    subprocess.run(["dropdb", "--if-exists", BASE_DATABASE], check=True, cwd=ODOO_BIN.parent)
    command = [
        sys.executable,
        str(ODOO_BIN),
        f"--database={BASE_DATABASE}",
        "--init=website",
        "--stop-after-init",
        "--no-http",
        *GENERIC_ODOO_ARGS,
    ]
    subprocess.run(command, check=True, cwd=ODOO_BIN.parent)


def copy_database(target):
    subprocess.run(["dropdb", "--if-exists", target], check=True, cwd=ODOO_BIN.parent)
    subprocess.run(["createdb", "--template", BASE_DATABASE, target], check=True, cwd=ODOO_BIN.parent)


def start_odoo():
    command = [
        sys.executable,
        str(ODOO_BIN),
        "--http-interface=localhost",
        f"--http-port={HTTP_PORT}",
        f"--database={DATABASE}",
        *GENERIC_ODOO_ARGS,
    ]
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
    deadline = time.time() + 300
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
    response = session.post(url, json={"jsonrpc": "2.0", "method": "call", "params": params, "id": 1}, timeout=timeout)
    response.raise_for_status()
    payload = response.json()
    if payload.get("error"):
        raise RuntimeError(json.dumps(payload["error"], indent=2))
    return payload["result"]


def login(session):
    session_info = jsonrpc(
        session,
        f"{BASE_URL}/web/session/authenticate",
        {"db": DATABASE, "login": LOGIN, "password": PASSWORD},
    )
    if not session_info.get("uid"):
        raise RuntimeError("Login failed.")
    return session_info


def create_website(session, name, domain):
    """Create a website: themes are stored per website, and its ``domain``
    lets the anonymous download reach it through the ``Host`` header."""
    return jsonrpc(
        session,
        f"{BASE_URL}/web/dataset/call_kw/website/create",
        {
            "model": "website",
            "method": "create",
            "args": [{"name": name, "domain": domain}],
            "kwargs": {},
        },
    )


def generate_website(session, context, theme_name, website_id, selected_palette, is_dark_palette):
    kwargs = {
        **CONFIGURATOR_VALUES,
        "theme_name": theme_name,
        "selected_palette": selected_palette,
        "is_dark_palette": is_dark_palette,
        "context": {**context, "website_id": website_id},
    }
    return jsonrpc(
        session,
        f"{BASE_URL}/web/dataset/call_kw/website/configurator_apply",
        {
            "model": "website",
            "method": "configurator_apply",
            "args": [],
            "kwargs": kwargs,
        },
        timeout=600,
    )


def create_menu_items(session, context, website_id):
    website = jsonrpc(
        session,
        f"{BASE_URL}/web/dataset/call_kw/website/read",
        {
            "model": "website",
            "method": "read",
            "args": [[website_id], ["menu_id"]],
            "kwargs": {"context": context},
        },
    )[0]
    jsonrpc(
        session,
        f"{BASE_URL}/web/dataset/call_kw/website.menu/create",
        {
            "model": "website.menu",
            "method": "create",
            "args": [[
                {
                    "name": title,
                    "url": url,
                    "website_id": website_id,
                    "parent_id": website["menu_id"][0],
                }
                for title, url in MENU_ITEMS
            ]],
            "kwargs": {"context": context},
        },
    )


def fetch_theme_image_urls(session, context):
    """Map theme attachment keys to their static image URLs. Records of every
    applied theme are returned, the latest applied one last."""
    records = jsonrpc(
        session,
        f"{BASE_URL}/web/dataset/call_kw/theme.ir.attachment/search_read",
        {
            "model": "theme.ir.attachment",
            "method": "search_read",
            "args": [
                [["key", "!=", False], ["url", "!=", False]],
                ["key", "url"],
            ],
            "kwargs": {"context": context},
        },
    )
    return {record["key"]: record["url"] for record in records}


WEB_IMAGE_KEY_RE = re.compile(r"/web/image/([\w-]+\.[\w.-]+)")


def embed_theme_image_urls(soup, image_urls):
    """Point ``/web/image/<key>`` images (which only exist once the theme is
    installed) to the theme's static files, keeping the key in
    ``industry_image_key`` for the configurator to swap in industry images."""
    for tag in soup.find_all(True):
        for attribute in ("src", "style"):
            value = tag.get(attribute)
            if not value:
                continue
            for key in WEB_IMAGE_KEY_RE.findall(value):
                static_url = image_urls.get(key)
                if not static_url:
                    continue
                value = value.replace(f"/web/image/{key}", static_url)
                tag["industry_image_key"] = key
            tag[attribute] = value


def fetch(url):
    # External hosts (Google Fonts...) 404 on the theme's Host header.
    headers = {}
    if PREVIEW_HOST and urlparse(url).hostname == urlparse(BASE_URL).hostname:
        headers["Host"] = PREVIEW_HOST
    try:
        response = DOWNLOAD_SESSION.get(url, timeout=30, headers=headers)
        response.raise_for_status()
        return response.content
    except Exception as error:
        print(f"  WARN: {url} - {error}", file=sys.stderr)
        return None


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


def resolve_css_imports(css, base_url):
    def replace(match):
        url = match.group(1) or match.group(2)
        if not url:
            return ""
        raw = fetch(urljoin(base_url, url))
        if not raw:
            return ""
        return resolve_css_imports(raw.decode("utf-8", errors="replace"), urljoin(base_url, url))

    return re.sub(
        r'@import\s+(?:url\(["\']?([^)"\']+)["\']?\)|["\']([^"\']+)["\'])\s*;',
        replace,
        css,
    )


def resolve_css_urls(css, base_url, quote='"'):
    def replace(match):
        raw_url, _quote = get_css_url(match)
        if raw_url.startswith("data:"):
            return match.group(0)
        font_asset_url = get_stable_font_asset_url(raw_url)
        if font_asset_url:
            return f'url({quote}{font_asset_url}{quote})'
        # External URLs (e.g. fonts.gstatic.com/l/font?kit=..., no extension) stay absolute.
        if is_external_url(raw_url, base_url):
            return f'url({quote}{urljoin(base_url, raw_url)}{quote})'
        return f'url({quote}{root_relative_url(raw_url, base_url)}{quote})'

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


def hex_to_rgb(color):
    color = color.lstrip("#")
    return tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))


def tokenize_bootstrap_rgb_triplets(css_text):
    # Rounded: dark palettes compile to fractional channels.
    palette_rgb = {hex_to_rgb(colors[0]): css_var for css_var, colors in PALETTE_COLORS.items()}

    def replace(match):
        triplet = tuple(round(float(component)) for component in match.groups()[1:])
        css_var = palette_rgb.get(triplet)
        return f"{match.group(1)}var({css_var}-rgb)" if css_var else match.group(0)

    return PALETTE_RGB_RE.sub(replace, css_text)


def hex_to_hls(color):
    hue, lightness, saturation = colorsys.rgb_to_hls(*(channel / 255 for channel in hex_to_rgb(color)))
    return hue * 360, lightness * 100, saturation * 100


def apply_scss_color_shades(css_text):
    palette = [(css_var, colors[0].upper()) for css_var, colors in PALETTE_COLORS.items()]

    def replace(match):
        color = match.group(0)
        if color.startswith("url(") or color.upper() in {palette_color for _var, palette_color in palette}:
            return color
        rgb = hex_to_rgb(color)
        hue, lightness, saturation = hex_to_hls(color)
        hsl_matches = []
        for css_var, palette_color in palette:
            palette_rgb = hex_to_rgb(palette_color)
            palette_hue, palette_lightness, palette_saturation = hex_to_hls(palette_color)
            if palette_saturation < 5:
                continue
            for mixed_with, target in (("white", 255), ("black", 0)):
                spread = [channel - target for channel in palette_rgb]
                weight = sum((c - target) * d for c, d in zip(rgb, spread)) / sum(d * d for d in spread)
                if 0.02 < weight < 0.98 and all(abs(target + d * weight - c) <= 1 for c, d in zip(rgb, spread)):
                    return f"color-mix(in srgb, var({css_var}) {weight * 100:.1f}%, {mixed_with})"
            hue_gap = min(abs(hue - palette_hue), 360 - abs(hue - palette_hue))
            if hue_gap <= 3 and abs(saturation - palette_saturation) <= 3:
                hsl_matches.append((hue_gap + abs(saturation - palette_saturation), css_var, lightness - palette_lightness))
        if not hsl_matches:
            return color
        _gap, css_var, lightness_delta = min(hsl_matches)
        if abs(lightness_delta) < 0.5:
            return f"var({css_var})"
        return f"hsl(from var({css_var}) h s calc(l {'+' if lightness_delta > 0 else '-'} {abs(lightness_delta):.2f}))"

    return DERIVED_COLOR_RE.sub(replace, css_text)


def apply_bootstrap_text_contrast(css_text):
    # Bootstrap picks white or #212529 text for a background at compile time
    # (white while contrast > $min-contrast-ratio 2.9, i.e. CIELAB L < 62.7):
    # redo that pick in CSS so it follows the selected palette's background.
    white = {"#FFFFFF", "#FFF", "WHITE"} | {f"VAR({css_var})".upper() for css_var, colors in PALETTE_COLORS.items() if colors[0] == "#FFFFFF"}

    def contrast_background_name(name):
        if name in ("color", "--color"):
            return name.replace("color", "background-color")
        if name.startswith("--btn") and name.endswith("-color"):
            return name.removesuffix("color") + "bg"
        if re.fullmatch(r"--o-cc\d-btn-(primary|secondary)-text", name):
            return name.removesuffix("-text")
        return None

    def replace_block(block):
        declarations = dict(re.findall(r"([-\w]+)\s*:\s*([^;{}]+)", block.group(0)))

        def replace_declaration(declaration):
            name, value = declaration.group(1), declaration.group(2)
            text, important = value.removesuffix("!important").strip(), value.strip().endswith("!important")
            background = declarations.get(contrast_background_name(name) or "", "").removesuffix("!important").strip()
            is_pick = text.upper() == "#212529" or (text.upper() in white and name not in ("color", "--color"))
            if not is_pick or "var(--" not in background:
                return declaration.group(0)
            pick = "(62.7 - l) * infinity"
            contrast = f"lab(from {background} clamp(14.4, {pick}, 100) clamp(-1.07, {pick}, 0) clamp(-3.32, {pick}, 0) / 1)"
            return f"{name}: {contrast}{' !important' if important else ''}"

        return re.sub(r"([-\w]+)\s*:\s*([^;{}]+)", replace_declaration, block.group(0))

    return re.sub(r"\{[^{}]*\}", replace_block, css_text)


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


def replace_palette_colors_in_urls(text):
    def replace(match):
        raw_url, quote = get_css_url(match)
        if raw_url.startswith("data:"):
            # Inline SVG icons need real colors, not palette tokens.
            return match.group(0)
        for css_var, colors in PALETTE_COLORS.items():
            for color in colors:
                raw_url = replace_color_token(raw_url, "%23" + color.lstrip("#"), css_var.removeprefix("--"))
        return f"url({quote}{raw_url}{quote})"

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


def check_palette_compiled_as_expected(soup):
    css_text = "".join(style.string or "" for style in soup.find_all("style"))
    for css_var, colors in PALETTE_COLORS.items():
        color = colors[0]
        if not re.search(rf"{re.escape(css_var)}\s*:\s*{re.escape(color)}{COLOR_TOKEN_END}", css_text, re.I):
            raise RuntimeError(f"{css_var}: {color} not found in the compiled :root CSS.")


def append_style(soup, style_id, css_text):
    style = soup.new_tag("style")
    style["id"] = style_id
    style.string = css_text
    soup.head.append(style)


def inject_palette_variables(soup):
    append_style(soup, "preview-palette-vars", ":root{" + " ".join(
        f"{css_var}: {colors[0]}; {css_var}-rgb: {', '.join(map(str, hex_to_rgb(colors[0])))};"
        for css_var, colors in PALETTE_COLORS.items()
    ) + "}")


def inject_color_combination_text_overrides(soup):
    heading_selectors = "h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6"
    rules = []
    for index in range(1, 6):
        text_color = f"var(--o-cc{index}-text)"
        rules.append(f".o_cc{index}{{--color:{text_color};color:{text_color};}}")
        rules.append(
            f".o_cc{index} :is({heading_selectors}),"
            f".o_colored_level .o_cc{index} :is({heading_selectors})"
            f"{{color:{text_color};}}",
        )

    append_style(soup, "preview-color-combination-text-overrides", "".join(rules))


def convert_vh_to_vw(css_text):
    return VH_RE.sub(lambda match: f"{float(match.group(1)) * VH_TO_VW_RATIO:g}vw", css_text)


def remove_parallax_fixed_background(css_text):
    def replace(match):
        selector, body = match.groups()
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
    css_text = replace_palette_colors_in_css(css_text)
    css_text = tokenize_bootstrap_rgb_triplets(css_text)
    css_text = apply_scss_color_shades(css_text)
    return apply_bootstrap_text_contrast(css_text)


def inline_stylesheets(soup, base_url):
    links = soup.find_all("link", rel=lambda rel: rel and "stylesheet" in rel)

    def fetch_link(link):
        href = link.get("href")
        if not href:
            return link, None, None
        abs_url = urljoin(base_url, href)
        return link, abs_url, fetch(abs_url)

    with ThreadPoolExecutor(max_workers=STYLESHEET_FETCH_WORKERS) as executor:
        fetched = list(executor.map(fetch_link, links))

    for link, abs_url, raw in fetched:
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
        # Single quotes: the url() ends up in a double-quoted style attribute.
        style = resolve_css_urls(tag["style"], base_url, quote="'")
        style = convert_vh_to_vw(style)
        tag["style"] = replace_palette_colors_in_style(style)


def inline_images(soup, base_url):
    for image in soup.find_all("img"):
        src = image.get("src", "")
        if src:
            src = root_relative_url(src, base_url)
            if WEBSITE_LOGO_URL_RE.match(src):
                src = DEFAULT_WEBSITE_LOGO_URL
            image["src"] = src
        image.attrs.pop("srcset", None)

    for source in soup.find_all("source"):
        source.attrs.pop("srcset", None)


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
        if {value.lower() for value in link.get("rel", [])} & {"canonical", "apple-touch-icon", "icon"}:
            link.decompose()
    for meta in soup.find_all("meta", attrs={"http-equiv": True}):
        if meta["http-equiv"].lower() in ("refresh", "content-security-policy"):
            meta.decompose()


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


def remove_javascript_dependent_classes(soup):
    # These classes hide elements until the frontend JS (absent here) runs.
    for removed_class in ("o_animate", "o_menu_loading"):
        for tag in soup.select(f".{removed_class}"):
            classes = [class_name for class_name in tag.get("class", []) if class_name != removed_class]
            if classes:
                tag["class"] = classes
            else:
                tag.attrs.pop("class", None)


# The static chart the builder's snippet dialog shows (s_numbers_charts).
CHART_PLACEHOLDER_SVG = """
<svg class="d-block mt-3 mx-auto" width="450" height="230" viewBox="0 0 100 110" xmlns="http://www.w3.org/2000/svg">
    <circle cx="50" cy="50" r="40" fill="transparent" stroke="transparent" stroke-width="25"/>
    <circle cx="50" cy="55" r="40" fill="transparent" stroke="var(--o-color-5)" stroke-width="25" stroke-dasharray="251.2" stroke-dashoffset="62.8"/>
</svg>
"""


def replace_chart_canvases(soup):
    # Chart.js paints the canvas at runtime; there is no JS here.
    for canvas in soup.select(".s_chart canvas"):
        canvas.replace_with(BeautifulSoup(CHART_PLACEHOLDER_SVG, "html.parser").find("svg"))


def fix_floating_blocks_preview(soup):
    # Reveal the blocks (opacity:0 until JS runs) and fake their overlapping stack.
    if not soup.select_one(".s_floating_blocks"):
        return
    append_style(soup, "preview-floating-blocks", (
        ".s_floating_blocks .s_floating_blocks_block"
        "{opacity:1!important;position:relative!important}"
        ".s_floating_blocks .s_floating_blocks_block:nth-child(1)"
        "{z-index:1;transform:scale(.96)!important}"
        ".s_floating_blocks .s_floating_blocks_block:nth-child(2)"
        "{z-index:2;transform:scale(.98)!important;margin-top:-45%!important}"
        ".s_floating_blocks .s_floating_blocks_block:nth-child(3)"
        "{z-index:3;margin-top:-45%!important}"
    ))


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


# The preview iframe is never narrower than this, and never interactive
# (``pe-none``): rules for smaller screens or hover/focus states never apply.
PREVIEW_MIN_WIDTH = 1440
INTERACTIVE_PSEUDO_RE = re.compile(r":(hover|focus|focus-visible|focus-within|active|visited)(?![\w-])")


def _needs_interaction(selector):
    """Whether ``selector`` only matches on hover/focus. Pseudo-class arguments
    are ignored: ``:not(:focus)`` matches without interaction."""
    while (top_level := re.sub(r"\([^()]*\)", "", selector)) != selector:
        selector = top_level
    return bool(INTERACTIVE_PSEUDO_RE.search(selector))


def _media_never_matches(prelude):
    """Whether no query of an ``@media`` prelude can match in the preview:
    print only, or narrower than ``PREVIEW_MIN_WIDTH`` (queries with ``not`` are kept)."""
    def never(query):
        query = query.lower()
        if "not " in query:
            return False
        return (bool(re.search(r"\bprint\b", query)) and not re.search(r"\b(screen|all)\b", query)) or any(
            float(width) < PREVIEW_MIN_WIDTH for width in re.findall(r"max-width\s*:\s*([\d.]+)px", query)
        )
    return all(never(query) for query in _split_top_level(prelude.removeprefix("@media"), ","))


def _purge_css_text(css, matcher):
    """Drop comments, the selectors no element matches or that only apply on
    hover/focus, the rules left without selectors and the ``@media`` blocks
    the preview can never match."""
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
            position = _skip_comment(css, position)
            continue

        if css[position] == "@":
            at_start = position
            position += 1
            while position < len(css) and (css[position].isalpha() or css[position] == "-"):
                position += 1
            keyword = css[at_start + 1:position].lower()
            brace, semicolon = css.find("{", position), css.find(";", position)
            if semicolon != -1 and (brace == -1 or semicolon < brace):
                # Statement at-rule (@import, @charset, @layer a, b;...).
                result.append(css[whitespace_start:semicolon + 1])
                position = semicolon + 1
                continue
            if brace == -1:
                result.append(css[whitespace_start:])
                break
            end = _find_block_end(css, brace)
            if keyword in AT_RULE_NESTING_KEYWORDS:
                never = keyword == "media" and _media_never_matches(css[at_start:brace])
                body = "" if never else _purge_css_text(css[brace + 1:end - 1], matcher)
                if body.strip():
                    result.append(f"{css[whitespace_start:brace]}{{{body}}}")
            else:
                result.append(css[whitespace_start:end])
            position = end
            continue

        brace = css.find("{", position)
        if brace == -1:
            result.append(css[whitespace_start:])
            break
        end = _find_block_end(css, brace)
        selectors = [
            selector for selector in _split_top_level(css[position:brace], ",")
            if not _needs_interaction(selector) and matcher.targets(" ".join(selector.split()))
        ]
        if selectors or not css[position:brace].strip():
            result.append(f"{css[whitespace_start:position]}{','.join(selectors)}{css[brace:end]}")
        position = end

    return "".join(result)


def _remove_unused_keyframes(css, referencing_text):
    """Drop the ``@keyframes`` whose name ``referencing_text`` never mentions."""
    result, position = [], 0
    for match in re.finditer(r"@(?:-\w+-)?keyframes\s+([\w-]+)\s*\{", css):
        if match.start() < position or re.search(rf"(?<![\w-]){re.escape(match.group(1))}(?![\w-])", referencing_text):
            continue
        result.append(css[position:match.start()])
        position = _find_block_end(css, match.end() - 1)
    return "".join(result) + css[position:]


def purge_unused_css(soup):
    matcher = _CssMatcher(soup)
    for style in soup.find_all("style"):
        if style.string:
            style.string = _purge_css_text(style.string, matcher)
    # Keyframes are referenced by name from what is left, or from inline styles.
    css = "".join(style.string or "" for style in soup.find_all("style"))
    referencing_text = re.sub(r"@(?:-\w+-)?keyframes\s+[\w-]+", "", css) + " ".join(
        tag["style"] for tag in soup.find_all(style=True)
    )
    for style in soup.find_all("style"):
        if style.string:
            style.string = _remove_unused_keyframes(style.string, referencing_text)
        if not (style.string or "").strip():
            style.decompose()


def _split_top_level(text, separator):
    """Split ``text`` on top-level ``separator``s: a separator inside a string,
    a comment or parens (data URIs contain ``;``) does not split."""
    parts, depth, start, position = [], 0, 0, 0
    while position < len(text):
        char = text[position]
        if char in ('"', "'"):
            position = _skip_string(text, position)
            continue
        if char == "/" and text[position + 1:position + 2] == "*":
            position = _skip_comment(text, position)
            continue
        if char in "([":
            depth += 1
        elif char in ")]":
            depth -= 1
        elif char == separator and depth <= 0:
            parts.append(text[start:position])
            position += 1
            start = position
            continue
        position += 1
    parts.append(text[start:position])
    return [part.strip() for part in parts if part.strip()]


AT_RULE_NESTING_KEYWORDS = ("media", "supports", "container", "layer", "document")


def _css_blocks(css_text, context=()):
    """Yield ``(context, head, body)`` for each rule or at-rule of ``css_text``,
    descending into ``@media``-like blocks, whose preludes make ``context``."""
    css_text = re.sub(r"/\*.*?\*/", "", css_text, flags=re.S)
    position = 0
    while (brace := css_text.find("{", position)) != -1:
        head = css_text[position:brace].strip()
        head = head[head.rfind(";") + 1:].strip()
        position = _find_block_end(css_text, brace)
        body = css_text[brace + 1:position - 1]
        keyword = head[1:].split(None, 1)[0].split("(")[0].lower() if head.startswith("@") else ""
        if keyword in AT_RULE_NESTING_KEYWORDS:
            yield from _css_blocks(body, context + (" ".join(head.split()),))
        else:
            yield context, head, body


def _parse_css_declarations(css_text):
    """Flatten ``css_text`` into ordered ``(context, selector, prop, value,
    important)`` tuples, one per selector of each rule."""
    declarations = []
    for context, head, body in _css_blocks(css_text):
        if head.startswith("@"):
            continue
        for selector in _split_top_level(head, ","):
            selector = " ".join(selector.split())
            for raw_declaration in _split_top_level(body, ";"):
                if ":" not in raw_declaration:
                    continue
                prop, _, value = raw_declaration.partition(":")
                value = value.strip()
                important = bool(re.search(r"!\s*important\s*$", value, re.I))
                value = re.sub(r"\s*!\s*important\s*$", "", value, flags=re.I)
                declarations.append((context, selector, prop.strip().lower(), value, important))
    return declarations


def _parse_at_rule_blocks(css_text):
    """``(context, keyword, head, text)`` of the ``@font-face`` and
    ``@keyframes`` blocks, which are compared as a whole."""
    blocks = []
    for context, head, body in _css_blocks(css_text):
        keyword = head[1:].split(None, 1)[0].split("(")[0].lower() if head.startswith("@") else ""
        if keyword == "font-face" or keyword.endswith("keyframes"):
            blocks.append((context, "font-face" if keyword == "font-face" else "keyframes", head, f"{head}{{{body}}}"))
    return blocks


def _collapse_declarations(declarations):
    """Keep only the last occurrence of each ``(context, selector, prop,
    important)``: the earlier ones always lose to it."""
    last_index = {}
    for index, declaration in enumerate(declarations):
        last_index[declaration[0], declaration[1], declaration[2], declaration[4]] = index
    return [declaration for index, declaration in enumerate(declarations)
            if last_index[declaration[0], declaration[1], declaration[2], declaration[4]] == index]


def _property_family(prop):
    # Custom properties are their own family; vendor-prefixed longhands share
    # the unprefixed family (``-webkit-transform`` -> ``transform``).
    if prop.startswith("--"):
        return prop
    return re.sub(r"^-(webkit|moz|ms|o)-", "", prop).split("-")[0]


_COMBINATOR_TOKENS = {">", "+", "~"}


def _fill_empty_compounds(selector):
    """Fill the compounds emptied by stripping pseudo-classes with ``*``, e.g.
    ``"> ~ label"`` -> ``"* > * ~ label"``."""
    tokens = selector.split()
    if not tokens:
        return "*"
    filled = ["*"] if tokens[0] in _COMBINATOR_TOKENS else []
    for index, token in enumerate(tokens):
        filled.append(token)
        if token in _COMBINATOR_TOKENS and (index + 1 == len(tokens) or tokens[index + 1] in _COMBINATOR_TOKENS):
            filled.append("*")
    return " ".join(filled)


class _CssMatcher:
    """The ``(id(element), pseudo-element)`` pairs a selector targets in a
    soup, pseudo-classes ignored. Unparsable selectors match everything:
    over-matching only makes the diff bigger."""

    def __init__(self, soup):
        self._soup = soup
        self._cache = {}

    def targets(self, selector):
        if selector not in self._cache:
            pseudo_element = PSEUDO_ELEMENT_RE.search(selector)
            try:
                elements = self._soup.select(_fill_empty_compounds(PSEUDO_RE.sub("", selector).strip()))
            except Exception:
                elements = self._soup.find_all(True)
            self._cache[selector] = {
                (id(element), pseudo_element.group(0) if pseudo_element else "") for element in elements
            }
        return self._cache[selector]


def _selector_specificity(selector):
    """``(ids, classes, types)`` of one selector: ``:where()`` counts zero,
    ``:is()``/``:not()``/``:has()`` count their most specific argument."""
    ids = classes = types = 0
    position = 0
    while position < len(selector):
        char = selector[position]
        name = re.match(r"(?:[\w-]|\\.)+", selector[position + 1:])
        if char == "#" and name:
            ids += 1
            position += 1 + name.end()
        elif char == "." and name:
            classes += 1
            position += 1 + name.end()
        elif char == "[":
            classes += 1
            position = selector.find("]", position) + 1 or len(selector)
        elif char == ":":
            is_element = selector[position + 1:position + 2] == ":"
            name = re.match(r":?([\w-]+)", selector[position + 1:])
            position += 1 + (name.end() if name else 0)
            arguments = ""
            if selector[position:position + 1] == "(":
                end = _find_block_end(selector.replace("(", "{").replace(")", "}"), position)
                arguments = selector[position + 1:end - 1]
                position = end
            pseudo = name.group(1).lower() if name else ""
            if is_element or pseudo in ("before", "after", "first-line", "first-letter"):
                types += 1
            elif pseudo in ("is", "not", "has", "matches"):
                arguments_ids, arguments_classes, arguments_types = max(
                    map(_selector_specificity, _split_top_level(arguments, ",")), default=(0, 0, 0),
                )
                ids, classes, types = ids + arguments_ids, classes + arguments_classes, types + arguments_types
            elif pseudo != "where":
                classes += 1
        elif char.isalpha():
            types += 1
            position += re.match(r"(?:[\w-]|\\.)+", selector[position:]).end()
        else:
            position += 1
    return ids, classes, types


def _expand_dark_diff(light_declarations, dark_declarations, matcher):
    """Resets for declarations removed in dark, then the dark declarations to
    append, in dark order: the changed ones, plus each unchanged one that an
    appended declaration of the same property family, importance and targets
    would now wrongly beat -- a changed one of equal specificity that came
    before it in dark, or a reset at least as specific. Repeat until nothing
    new is appended."""
    light_declarations = _collapse_declarations(light_declarations)
    dark_declarations = _collapse_declarations(dark_declarations)
    light_set = set(light_declarations)
    dark_keys = {(context, selector, prop, important)
                 for context, selector, prop, _value, important in dark_declarations}
    changed = [declaration for declaration in dark_declarations if declaration not in light_set]
    removed = [declaration for declaration in light_declarations
               if (declaration[0], declaration[1], declaration[2], declaration[4]) not in dark_keys]

    resets = [
        (context, selector, prop, "unset", important)
        for context, selector, prop, _value, important in removed
        if matcher.targets(selector)
    ]
    dark_order = {declaration: index for index, declaration in enumerate(dark_declarations)}
    # (specificity, dark position or None for a reset, targets) by (family, importance).
    appended = defaultdict(list)

    def append(declaration, position):
        _context, selector, prop, _value, important = declaration
        appended[_property_family(prop), important].append(
            (_selector_specificity(selector), position, matcher.targets(selector)),
        )

    for declaration in resets:
        append(declaration, None)
    emitted = {declaration for declaration in changed if matcher.targets(declaration[1])}
    for declaration in emitted:
        append(declaration, dark_order[declaration])

    def is_beaten(declaration):
        _context, selector, prop, _value, important = declaration
        specificity, position, targets = _selector_specificity(selector), dark_order[declaration], matcher.targets(selector)
        return any(
            (other_specificity >= specificity if other_position is None
             else other_specificity == specificity and other_position < position)
            and other_targets & targets
            for other_specificity, other_position, other_targets in appended[_property_family(prop), important]
        )

    while True:
        beaten = [
            declaration for declaration in dark_declarations
            if declaration not in emitted and matcher.targets(declaration[1]) and is_beaten(declaration)
        ]
        if not beaten:
            break
        for declaration in beaten:
            emitted.add(declaration)
            append(declaration, dark_order[declaration])

    return resets, [declaration for declaration in dark_declarations if declaration in emitted]


def _diff_at_rule_blocks(light_blocks, dark_blocks):
    """New ``@font-face``s and new-or-changed ``@keyframes``, as ``(context,
    text)`` whole blocks to emit."""
    def normalize(text):
        # Bundle URLs embed the id of the website each variant was rendered on.
        return " ".join(re.sub(r"/web/assets/\d+/", "/web/assets/", text).split())

    light_font_faces = {normalize(text) for _context, keyword, _head, text in light_blocks if keyword == "font-face"}
    # Only the last @keyframes of a name applies.
    light_keyframes = {(context, head): normalize(text) for context, keyword, head, text in light_blocks if keyword == "keyframes"}
    dark_keyframes = {(context, head): text for context, keyword, head, text in dark_blocks if keyword == "keyframes"}
    emitted = [
        (context, text) for context, keyword, _head, text in dark_blocks
        if keyword == "font-face" and normalize(text) not in light_font_faces
    ]
    emitted += [
        (context, text) for (context, head), text in dark_keyframes.items()
        if light_keyframes.get((context, head)) != normalize(text)
    ]
    return emitted


def _wrap_in_context(context, css_text):
    for prelude in reversed(context):
        css_text = f"{prelude}{{{css_text}}}"
    return css_text


def _render_declarations(declarations):
    """Render declaration tuples as CSS, grouping consecutive ones by context
    and selector, and consecutive rules with the same body in one selector list."""
    rendered = ""
    for context, context_declarations in groupby(declarations, key=lambda declaration: declaration[0]):
        rules = []
        for selector, selector_declarations in groupby(context_declarations, key=lambda declaration: declaration[1]):
            properties = "".join(
                f"{prop}: {value}{' !important' if important else ''};"
                for _context, _selector, prop, value, important in selector_declarations
            )
            if rules and rules[-1][1] == properties:
                rules[-1][0].append(selector)
            else:
                rules.append(([selector], properties))
        rendered += _wrap_in_context(context, "".join(
            f"{', '.join(selectors)}{{{properties}}}" for selectors, properties in rules
        ))
    return rendered


def build_dark_css_diff(light_css, dark_css, dark_soup):
    """CSS that, appended after ``light_css`` on ``dark_soup``, reproduces
    ``dark_css``'s cascade there."""
    matcher = _CssMatcher(dark_soup)
    resets, emitted = _expand_dark_diff(_parse_css_declarations(light_css), _parse_css_declarations(dark_css), matcher)
    return _render_declarations(resets + emitted) + "".join(
        _wrap_in_context(context, text)
        for context, text in _diff_at_rule_blocks(_parse_at_rule_blocks(light_css), _parse_at_rule_blocks(dark_css))
    )


def remove_blank_lines(soup):
    # The purge leaves the whitespace around the rules it drops.
    for style in soup.find_all("style"):
        if style.string:
            style.string = re.sub(r"\n[ \t]*(?=\n)", "", style.string)


def collect_style_css(soup):
    return "\n".join(style.string or "" for style in soup.find_all("style"))


FONT_FACE_RE = re.compile(r"@font-face\s*\{([^{}]*)\}")
# Elements the browser styles bold or italic by default.
BOLD_TAGS = ("b", "strong", "h1", "h2", "h3", "h4", "h5", "h6", "th")
ITALIC_TAGS = ("em", "i", "cite", "var", "dfn", "address")


def _font_face_value(body, name):
    match = re.search(rf"(?:^|;)\s*{name}\s*:\s*([^;]+)", body)
    return match.group(1).strip() if match else ""


def _font_face_key(body):
    return (
        _font_face_value(body, "font-family").strip("'\"").lower(),
        _font_face_value(body, "font-style") or "normal",
        _font_weight_number(_font_face_value(body, "font-weight") or "normal"),
    )


def _font_weight_number(value):
    value = value.strip().lower()
    return {"normal": 400, "bold": 700}.get(value) or (int(value) if value.isdigit() else None)


def _picked_font_weight(weight, available):
    """The weight among ``available`` a browser uses for ``weight`` (CSS Fonts
    font-weight matching)."""
    lighter = sorted((other for other in available if other < weight), reverse=True)
    if 400 <= weight <= 500:
        order = sorted(other for other in available if weight <= other <= 500) + lighter
        order += sorted(other for other in available if other > 500)
    elif weight < 400:
        order = ([weight] if weight in available else []) + lighter + sorted(other for other in available if other > weight)
    else:
        order = sorted(other for other in available if other >= weight) + lighter
    return order[0] if order else None


def _unicode_range_matches(unicode_range, characters):
    if not unicode_range:
        return True
    for part in unicode_range.split(","):
        start, _, end = part.strip()[2:].partition("-")
        low, high = int(start.replace("?", "0"), 16), int((end or start).replace("?", "F"), 16)
        if any(low <= character <= high for character in characters):
            return True
    return False


def remove_unused_font_faces(css_texts, declarations, soups):
    """Remove from ``css_texts`` the ``@font-face`` rules ``soups`` never use:
    unnamed families, unused unicode ranges, italics or weights."""
    matchers = [_CssMatcher(soup) for soup in soups]
    matched = [
        declaration for declaration in declarations
        if declaration[2].startswith("--") or any(matcher.targets(declaration[1]) for matcher in matchers)
    ]

    def values(*props, custom=None):
        return [
            value.lower() for _context, _selector, prop, value, _important in matched
            if prop in props or (custom and prop.startswith("--") and custom in prop)
        ]

    family_text = " ".join(values("font-family", "font", custom="-"))
    # Empty ``<i>`` are icons, not italic text.
    italic = any("italic" in value or "oblique" in value for value in values("font-style", "font", custom="style")) or any(
        tag.get_text(strip=True) for soup in soups for tag in soup.find_all(ITALIC_TAGS)
    )
    weights, any_weight = {400}, False
    for value in values("font-weight", "font", custom="weight"):
        for token in re.findall(r"var\(\s*(--[\w-]+)|([\w-]+)", value):
            if (token[0] and "weight" not in token[0]) or token[1] in ("bolder", "lighter"):
                any_weight = True
            elif token[1] and (weight := _font_weight_number(token[1])) and 100 <= weight <= 1000:
                weights.add(weight)
    if any(soup.find(BOLD_TAGS) for soup in soups):
        weights.add(700)

    characters = set()
    for soup in soups:
        body = soup.body or soup
        characters.update(map(ord, " ".join(
            text for text in body.find_all(string=True) if text.parent.name not in ("style", "script")
        )))
        for tag in body.find_all(True):
            for attribute in ("placeholder", "value", "alt", "title"):
                if isinstance(tag.get(attribute), str):
                    characters.update(map(ord, tag[attribute]))
    for value in values("content"):
        characters.update(int(code, 16) for code in re.findall(r"\\([0-9a-f]{1,6})", value))
        characters.update(map(ord, re.sub(r"\\[0-9a-f]{1,6}\s?", "", value)))

    available = defaultdict(set)
    for css_text in css_texts:
        for body in FONT_FACE_RE.findall(css_text):
            family, style, weight = _font_face_key(body)
            if weight:
                available[family, style].add(weight)

    def is_used(body):
        family, style, weight = _font_face_key(body)
        return (
            family in family_text
            and (style == "normal" or italic)
            and _unicode_range_matches(_font_face_value(body, "unicode-range"), characters)
            # A weight range (variable font) is kept as is.
            and (any_weight or weight is None
                 or weight in {_picked_font_weight(used, available[family, style]) for used in weights})
        )

    return [
        FONT_FACE_RE.sub(lambda match: match.group(0) if is_used(match.group(1)) else "", css_text)
        for css_text in css_texts
    ]


def download_static_html(url, theme_image_urls, label):
    """Download the generated homepage as a self-contained soup."""
    start = time.perf_counter()
    raw = fetch(url)
    if not raw:
        raise RuntimeError("Could not download the generated website.")
    print(f"[{label}] Downloaded {url} ({len(raw) // 1024} KB) in {elapsed(start)}")

    step = time.perf_counter()
    soup = BeautifulSoup(raw, "html.parser")
    inline_stylesheets(soup, url)
    inline_style_blocks(soup, url)
    print(f"[{label}] Stylesheets downloaded and processed in {elapsed(step)}")
    inline_inline_styles(soup, url)
    inline_images(soup, url)
    inline_font_preloads(soup, url)
    remove_preview_metadata(soup)
    replace_palette_colors_in_attributes(soup)
    embed_theme_image_urls(soup, theme_image_urls)
    remove_javascript(soup)
    remove_javascript_dependent_classes(soup)
    replace_chart_canvases(soup)
    step = time.perf_counter()
    purge_unused_css(soup)
    print(f"[{label}] Unused CSS purged in {elapsed(step)} ({len(collect_style_css(soup)) // 1024} KB left)")
    fix_floating_blocks_preview(soup)
    check_palette_compiled_as_expected(soup)
    inject_palette_variables(soup)
    inject_color_combination_text_overrides(soup)
    return soup


def get_generated_page_url(result):
    action = result.get("url")
    path = action if isinstance(action, str) else isinstance(action, dict) and action.get("params", {}).get("path")
    return urljoin(f"{BASE_URL}/", path or "/")


def theme_host(theme_name, suffix):
    # Hostnames can't contain underscores.
    return f"{theme_name.replace('_', '-')}{suffix}.localhost:{urlparse(BASE_URL).port or 80}"


def generate_theme_preview(session, context, theme_dir):
    theme_name = theme_dir.name
    global PALETTE_COLORS, PREVIEW_HOST

    theme_start = time.perf_counter()
    soups = []
    for suffix, palette, selected_palette, is_dark_palette in PREVIEW_VARIANTS:
        label = f"{theme_name}{suffix}"
        PALETTE_COLORS = palette

        step = time.perf_counter()
        host = theme_host(theme_name, suffix)
        website_id = create_website(session, label, f"http://{host}")
        result = generate_website(session, context, theme_name, website_id, selected_palette, is_dark_palette)
        create_menu_items(session, context, website_id)
        print(f"[{label}] Theme applied with the {selected_palette} palette in {elapsed(step)}")
        # After applying the theme, so its attachments are the latest ones.
        theme_image_urls = fetch_theme_image_urls(session, context)
        print(f"[{label}] {len(theme_image_urls)} theme images found")
        PREVIEW_HOST = host
        soups.append(download_static_html(get_generated_page_url(result), theme_image_urls, label))

    light_soup, dark_soup = soups
    step = time.perf_counter()
    light_css = collect_style_css(light_soup)
    css_diff = build_dark_css_diff(light_css, collect_style_css(dark_soup), dark_soup)
    print(f"[{theme_name}] Dark CSS diff built in {elapsed(step)} ({len(css_diff) // 1024} KB)")

    step = time.perf_counter()
    style_tags = [style for style in light_soup.find_all("style") if style.string]
    css_texts = [style.string for style in style_tags] + [css_diff]
    cleaned_texts = remove_unused_font_faces(
        css_texts,
        _parse_css_declarations(light_css) + _parse_css_declarations(css_diff),
        [light_soup, dark_soup],
    )
    *light_texts, css_diff = cleaned_texts
    for style, text in zip(style_tags, light_texts):
        style.string = text
    faces_before = sum(len(FONT_FACE_RE.findall(text)) for text in css_texts)
    faces_after = sum(len(FONT_FACE_RE.findall(text)) for text in cleaned_texts)
    print(f"[{theme_name}] Fonts cleaned in {elapsed(step)}: {faces_after}/{faces_before} @font-face kept")

    remove_blank_lines(light_soup)
    html_path = get_preview_output_path(theme_dir, "preview.html")
    html_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(str(light_soup), encoding="utf-8")
    css_path = get_preview_output_path(theme_dir, "preview_dark.css")
    css_path.write_text(css_diff, encoding="utf-8")
    print(
        f"[{theme_name}] Saved {html_path.name} ({html_path.stat().st_size // 1024} KB) and "
        f"{css_path.name} ({css_path.stat().st_size // 1024} KB) in {elapsed(theme_start)} total"
    )

    get_preview_output_path(theme_dir, "preview_dark.html").unlink(missing_ok=True)


def worker_database(worker_index):
    return f"{BASE_DATABASE}-{worker_index}"


def run_worker(worker_index, theme_names):
    """Boot one Odoo instance and generate the given themes on it."""
    global DATABASE, HTTP_PORT, BASE_URL
    HTTP_PORT = BASE_HTTP_PORT + worker_index
    BASE_URL = f"http://localhost:{HTTP_PORT}"
    DATABASE = worker_database(worker_index)

    time.sleep(worker_index * BOOT_STAGGER_SECONDS)
    worker_start = time.perf_counter()
    server = start_odoo()
    rpc_session = requests.Session()
    generated, failed = [], []
    try:
        wait_for_odoo(server)
        print(f"Worker {worker_index}: Odoo ready on port {HTTP_PORT} in {elapsed(worker_start)}")
        session_info = login(rpc_session)
        context = session_info.get("user_context", {})
        for name in theme_names:
            try:
                generate_theme_preview(rpc_session, context, THEMES_DIR / name)
                generated.append(name)
            except Exception as error:
                print(f"  ERROR {name}: {error}", file=sys.stderr)
                failed.append(name)
    finally:
        rpc_session.close()
        stop_odoo(server)
    print(f"Worker {worker_index}: {len(generated)} themes generated in {elapsed(worker_start)}")
    return generated, failed


def main():
    run_start = time.perf_counter()
    theme_names = [theme_dir.name for theme_dir in get_theme_dirs()]
    num_workers = max(1, min(NUM_WORKERS, len(theme_names)))
    shards = [[] for _ in range(num_workers)]
    for index, name in enumerate(theme_names):
        shards[index % num_workers].append(name)

    print(f"Generating {len(theme_names)} theme previews across {num_workers} worker(s).")

    # Sequential: concurrent template copies of the same database contend.
    step = time.perf_counter()
    prepare_base_database()
    for index in range(num_workers):
        copy_database(worker_database(index))
    print(f"Base database ready and copied for {num_workers} worker(s) in {elapsed(step)}")

    generated, failed = [], []
    if num_workers == 1:
        generated, failed = run_worker(0, shards[0])
    else:
        with ProcessPoolExecutor(max_workers=num_workers) as executor:
            futures = {
                executor.submit(run_worker, index, shard): index
                for index, shard in enumerate(shards)
                if shard
            }
            for future in as_completed(futures):
                index = futures[future]
                try:
                    worker_generated, worker_failed = future.result()
                    generated += worker_generated
                    failed += worker_failed
                except Exception as error:
                    print(f"Worker {index} crashed: {error}", file=sys.stderr)

    print(f"Done in {elapsed(run_start)}: {len(generated)} generated, {len(failed)} failed.")
    if failed:
        print("Failed: " + ", ".join(sorted(failed)), file=sys.stderr)


if __name__ == "__main__":
    main()
