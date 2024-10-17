# Part of Odoo. See LICENSE file for full copyright and licensing details.

from lxml import etree, html

import logging
import re

from odoo.addons.website.tools import MockRequest
from odoo.tests import tagged, TransactionCase
from odoo.tools import escape_psql

_logger = logging.getLogger(__name__)

CONFLICTUAL_CLASSES = [
    ['btn-outline-primary', 'btn-primary', 'btn-secondary'],
    ['btn-block', 'btn-outline-primary'],
    ['container', 'container-fluid', 'o_container_small'],
    ['d-block', 'd-flex', 'd-inline-block', 'd-none'],
    ['d-block', 'd-lg-block', 'd-md-block'],
    ['d-flex', 'd-md-flex'],
    ['flex-column', 'flex-column-reverse', 'flex-row', 'flex-row-reverse'],
    ['g-0', 'g-col-lg-2', 'g-col-lg-3', 'g-col-lg-4', 'g-col-lg-5', 'g-col-lg-6'],
    ['g-0', 'g-height-5', 'g-height-8', 'g-height-10'],
    ['h-100', 'o_half_screen_height', 'o_full_screen_height'],
    ['justify-content-center', 'justify-content-start'],
    ['nav-link', 'nav-pills', 'nav-tabs'],
    ['o_cc1', 'o_cc2', 'o_cc3', 'o_cc4', 'o_cc5'],
    ['o_spc-medium', 'o_spc-none', 'o_spc-small'],
    ['oi-arrows-h', 'oi-arrows-v', 'oi-chevron-left', 'oi-chevron-right', 'oi-search'],
    ['position-absolute', 'position-relative'],
    ['s_carousel_default', 's_carousel_rounded'],
    ['s_image_gallery_indicators_arrows_boxed', 's_image_gallery_indicators_arrows_rounded'],
    ['text-center', 'text-end', 'text-start'],
]

# For each RE, associates a whitelist
CONFLICTUAL_CLASSES_RE = {
    # Align
    re.compile(r'^align-(?!(self|items)-).+'): [],
    re.compile(r'^align-self-.+'): [],
    re.compile(r'^align-items-.+'): [],
    # BG
    re.compile(r'^bg(-|_)'): [
        'bg_option_menu_gradient',
    ],
    # Col
    re.compile(r'^col-\d+$'): [],
    re.compile(r'^col-lg-.+'): [],
    re.compile(r'^offset-\d+$'): [],
    re.compile(r'^offset-lg-.+'): [],
    # Display
    re.compile(r'^display-\d$'): [],
    re.compile(r'^display-\d-fs$'): [],
    # Margin, padding
    re.compile(r'^m-(\d|auto)$'): [],
    re.compile(r'^m(x|s)-\d$'): [],
    re.compile(r'^m(x|e)-\d$'): [],
    re.compile(r'^m(y|t)-\d$'): [],
    re.compile(r'^m(y|b)-\d$'): [],
    re.compile(r'^(p(x|s)?-?\d+|padding-.+)$'): [],
    re.compile(r'^(p(x|e)?-?\d+|padding-.+)$'): [],
    re.compile(r'^(p(y|t)?-?\d+|padding-.+)$'): [],
    # p0+pb32 appears in Bewise and Graphene
    re.compile(r'^(p(y|b)?-?\d+|padding-.+)$'): ['p0'],
    # Font awesome
    re.compile(r'^fa-\dx$'): [],
    # Whitelist workaround for s_social_media inner snippet Layout: None
    re.compile(r'^fa-...+'): ['fa-stack'],
    # Rounded
    re.compile(r'^rounded-.+'): [],
    # Shadow
    re.compile(r'^shadow-.+'): [],
    # Shapes
    re.compile(r'^o_web_editor_[A-Z].+'): [],
    # Snippets
    re.compile(r'^s_.*'): [
        's_alert_md',
        's_blockquote_with_icon', 's_blockquote',
        's_carousel_default', 's_carousel_rounded', 's_carousel_boxed',
        's_carousel_indicators_dots', 's_carousel_indicators_hidden', 's_carousel_controllers_indicators_outside',
        's_quotes_carousel',
        's_dynamic', 's_dynamic_empty',
        's_dynamic_snippet_blog_posts', 's_blog_posts_effect_marley', 's_blog_post_big_picture', 's_blog_posts_post_picture_size_default',
        's_event_upcoming_snippet', 's_event_event_picture',
        's_col_no_bgcolor', 's_col_no_resize',
        's_image_gallery', 's_image_gallery_indicators_arrows_boxed', 's_image_gallery_indicators_arrows_rounded',
        's_image_gallery_indicators_dots', 's_image_gallery_indicators_squared', 's_image_gallery_indicators_rounded', 's_image_gallery_indicators_hidden', 's_image_gallery_indicators_bars', 's_image_gallery_indicators_outside','s_image_gallery_controllers_outside_arrows_right', 's_image_gallery_controllers_outside',
        's_newsletter_list', 's_newsletter_subscribe_form',
        's_parallax_is_fixed', 's_parallax_no_overflow_hidden',
        's_process_steps_connector_line',
        's_product_catalog_dish_name', 's_product_catalog_dish_dot_leaders',
        's_progress_bar_label_hidden', 's_progress_bar_label_inline',
        's_rating_no_title',
        's_table_of_content_vertical_navbar', 's_table_of_content_navbar_sticky', 's_table_of_content_navbar_wrap',
        's_timeline_card',
        's_website_form_custom', 's_website_form_dnone', 's_website_form_field', 's_website_form_input', 's_website_form_mark', 's_website_form_submit', 's_website_form_no_submit_label',
        's_donation_btn', 's_donation_custom_btn',
    ],
    # Text
    re.compile(r'^text-(?!(center|end|start|bg-|lg-)).*$'): [
        'text-break', 'text-decoration-none', 'text-reset',
    ],
    re.compile(r'^text-bg-.*$'): [],
    re.compile(r'^text-lg-.*$'): [],
    # Width
    re.compile(r'^w-\d*$'): [],
}


@tagged('post_install', '-at_install')
class TestNewPageTemplates(TransactionCase):

    def test_template_names(self):
        websites_themes = self.env['website'].get_test_themes_websites()
        for website in websites_themes:
            views = self.env['ir.ui.view'].search([
                ('key', 'like', f'{website.theme_id.name}.new_page_template%_s_'),
            ])
            if website.theme_id.name != 'theme_default':
                self.assertGreater(len(views), 10, "Test should have encountered some views in theme %r" % website.name)
            for view in views:
                self.assertEqual(view.mode, 'extension', "Theme's new page template customization %r should never be primary" % view.key)
                name = view.key.split('.')[1]
                parent_name = view.inherit_id.key.split('.')[1]
                self.assertEqual(name, parent_name, "Theme's new page template customization %r should use the same name as their parent %r" % (view.key, view.inherit_id.key))

    def test_render_templates(self):
        errors = []
        view_ids = set()
        websites_themes = self.env['website'].get_test_themes_websites()
        for website in websites_themes:
            with MockRequest(self.env, website=website):
                views = self.env['ir.ui.view'].search([
                    '|', '|',
                    ('key', 'like', f'{website.theme_id.name}.s_'),
                    ('key', 'like', f'{website.theme_id.name}.configurator'),
                    ('key', 'like', f'{website.theme_id.name}.new_page'),
                ])
                view_ids.update(views.ids)
                for view in views:
                    try:
                        self.env['ir.qweb']._render(view.id)
                    except Exception:
                        errors.append("View %s cannot be rendered" % view.key)
        _logger.info("Tested %s views", len(view_ids))
        self.assertGreater(len(view_ids), 1250, "Test should have encountered a lot of views")
        self.assertFalse(errors, "No error should have been collected")

    def test_render_applied_templates(self):
        View = self.env['ir.ui.view']
        errors = []
        classes_inventory = set()
        view_count = 0

        def check(theme_name, website):
            with MockRequest(self.env, website=website):
                views = View.search([
                    '|', '|',
                    ('key', 'in', [
                        'website.snippets',
                        'website.new_page_template_groups',
                    ]),
                    ('key', 'like', escape_psql('website.configurator_')),
                    ('key', 'like', escape_psql('website.new_page_template_sections_')),
                ])
                for view in views:
                    try:
                        # TODO: Improve the perfs of the next line
                        #       Doesn't seem to be a way to avoid one RECURSIVE
                        #       SQL Query from `_get_inheriting_views` per view
                        html_text = self.env['ir.qweb']._render(view.id)
                        if not html_text:
                            continue
                        html_tree = html.fromstring(html_text)
                        blocks_el = html_tree.xpath("//*[@id='o_scroll']")
                        if blocks_el:
                            # Only look at blocks in website.snippets
                            html_tree = blocks_el[0]
                        for el in html_tree.xpath('//*[@class]'):
                            classes = el.attrib['class'].split()
                            classes_inventory.update(classes)
                            if len(classes) != len(set(classes)):
                                errors.append("Using %r, view %r contains duplicate classes: %r" % (theme_name, view.key, classes))
                            for conflicting_classes in CONFLICTUAL_CLASSES:
                                conflict = set(classes).intersection(conflicting_classes)
                                if len(conflict) > 1:
                                    errors.append("Using %r, view %r contains conflicting classes: %r in %r" % (theme_name, view.key, conflict, classes))
                            for conflicting_classes_re in CONFLICTUAL_CLASSES_RE:
                                conflict = {cl for cl in filter(conflicting_classes_re.findall, set(classes))}
                                white_list = CONFLICTUAL_CLASSES_RE[conflicting_classes_re]
                                conflict.difference_update(white_list)
                                if len(conflict) > 1:
                                    errors.append("Using %r, view %r contains conflicting classes: %r in %r (according to pattern %r)" % (theme_name, view.key, conflict, classes, conflicting_classes_re.pattern))
                        for el in html_tree.xpath('//*[@style]'):
                            styles = el.attrib['style'].split(';')
                            non_empty_styles = filter(lambda style: style, styles)
                            property_names = list(map(lambda style: style.split(':')[0].strip(), non_empty_styles))
                            if len(property_names) != len(set(property_names)):
                                errors.append("Using %r, view %r contains duplicate style properties: %r" % (theme_name, view.key, el.attrib['style']))
                        for grid_el in html_tree.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' o_grid_mode ')]"):
                            if 'data-row-count' not in grid_el.attrib:
                                errors.append("Using %r, view %r defines a grid mode row without row count" % (theme_name, view.key))
                                continue
                            row_count = int(grid_el.attrib['data-row-count'])
                            max_row = 0
                            for item_el in grid_el.xpath(".//div[contains(concat(' ', normalize-space(@class), ' '), ' o_grid_item ')]"):
                                classes = item_el.attrib['class'].split()
                                styles = item_el.attrib['style'].split(';')
                                grid_area_style = list(filter(lambda style: style.strip().startswith('grid-area:'), styles))
                                if not grid_area_style:
                                    errors.append("Using %r, view %r does not specify a grid-area for its grid item" % (theme_name, view.key))
                                    continue
                                grid_area = grid_area_style[0].split(':')[1].strip()
                                top, left, bottom, right = map(int, grid_area.split('/'))
                                max_row = max(max_row, bottom)
                                height_class = f'g-height-{bottom - top}'
                                if height_class not in classes:
                                    errors.append("Using %r, view %r does not specify %r for grid item %r (%r)" % (theme_name, view.key, height_class, grid_area, classes))
                                width_class = f'g-col-lg-{right - left}'
                                if width_class not in classes:
                                    errors.append("Using %r, view %r does not specify %r for grid item %r (%r)" % (theme_name, view.key, width_class, grid_area, classes))
                                non_grid_width_class = f'col-lg-{right - left}'
                                if non_grid_width_class not in classes:
                                    errors.append("Using %r, view %r does not specify %r for grid item %r (%r)" % (theme_name, view.key, non_grid_width_class, grid_area, classes))
                                padding_classes = list(filter(lambda klass: klass.startswith('pb') or klass.startswith('pt'), classes))
                                if padding_classes:
                                    errors.append("Using %r, view %r specifies unnecessary padding classes on grid item %r" % (theme_name, view.key, padding_classes))
                            if row_count != max_row - 1:
                                errors.append("Using %r, view %r defines %r as row count while %r is reached" % (theme_name, view.key, row_count, max_row))
                        for el in html_tree.xpath('//*[@data-row-count]'):
                            classes = el.attrib['class'].split()
                            if 'o_grid_mode' not in classes:
                                errors.append("Using %r, view %r defines a row count on a non-grid mode row" % (theme_name, view.key))
                    except Exception:
                        _logger.error("Using %r, view %r cannot be rendered", theme_name, view.key)
                        errors.append("Using %r, view %r cannot be rendered" % (theme_name, view.key))
                return len(views)

        view_count += check('no theme', self.env.ref('website.default_website'))
        websites_themes = self.env['website'].get_test_themes_websites()
        for website in websites_themes:
            view_count += check(website.name, website)
        _logger.info("Tested %s views", view_count)
        self.assertGreater(view_count, 2900, "Test should have checked many views")
        # Use this information to potentially update known possible conflicts.
        for known_classes in CONFLICTUAL_CLASSES:
            classes_inventory.difference_update(known_classes)
        for known_classes in CONFLICTUAL_CLASSES_RE.values():
            classes_inventory.difference_update(known_classes)
        for known_classes_re in CONFLICTUAL_CLASSES_RE:
            classes_inventory = [cl for cl in filter(lambda cl: not known_classes_re.findall(cl), classes_inventory)]
        _logger.info("Unknown classes encountered: %r", sorted(list(classes_inventory)))
        self.assertFalse(errors, "No error should have been collected")

    def test_attribute_separator(self):
        ATTRIBUTE_SEPARATORS = {
            'class': ' ',
            'style': ';',
            'sizes': ',',
            'itemref': ' ',
        }
        View = self.env['ir.ui.view']
        errors = []
        view_count = 0

        for module_name in ['website', *map(lambda website: website.theme_id.name, self.env['website'].get_test_themes_websites())]:
            views = View.search([
                '|', '|',
                ('key', 'like', escape_psql(f'{module_name}.s_')),
                ('key', 'like', escape_psql(f'{module_name}.configurator')),
                ('key', 'like', escape_psql(f'{module_name}.new_page')),
            ])
            for view in views:
                try:
                    xml_tree = etree.fromstring(view.arch_db)
                except etree.LxmlError:
                    _logger.error("Using %r, view %r cannot be parsed: %r", module_name, view.key, view.arch_db)
                    errors.append("Using %r, view %r cannot be parsed: %r" % (module_name, view.key, view.arch_db))
                    continue
                for el in xml_tree.xpath('//attribute[@add] | //attribute[@remove]'):
                    attribute_name = el.attrib['name']
                    if attribute_name in ATTRIBUTE_SEPARATORS:
                        current_separator = el.attrib.get('separator', ',')
                        expected_separator = ATTRIBUTE_SEPARATORS[attribute_name]
                        if current_separator != expected_separator:
                            errors.append("Using %r, view %r uses separator %r to modify attribute %r" % (module_name, view.key, current_separator, attribute_name))
            view_count += len(views)

        _logger.info("Tested %s views", view_count)
        self.assertGreater(view_count, 2500, "Test should have checked many views")
        self.assertFalse(errors, "No error should have been collected")
