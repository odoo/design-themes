# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests import standalone


@standalone('website_standalone')
def test_02_theme_default_generate_primary_templates(env):
    # Verify that theme default's configurator templates are created
    # on website update.
    theme_default = env.ref('base.module_theme_default')
    website_module = env.ref('base.module_website')

    if theme_default.state == 'installed':
        theme_default.button_immediate_uninstall()
    env['ir.ui.view'].with_context(_force_unlink=True).search([('key', 'like', 'website.configurator_')]).unlink()

    if website_module.state == 'installed':
        website_module.button_immediate_upgrade()
    else:
        website_module.button_immediate_install()

    template_keys = env['ir.ui.view'].search([('key', 'like', 'website.configurator')]).mapped('key')
    manifest = env['ir.module.module'].get_module_info('theme_default')
    snippets_per_page = manifest.get('configurator_snippets')
    for page in snippets_per_page:
        for snippet in snippets_per_page[page]:
            template_key = f'website.configurator_{page}_{snippet}'
            assert template_key in template_keys, f"{template_key} should exist"

    env['website'].with_context(website_id=1).configurator_apply(
        selected_features=[1, 2, 3, 4],
        industry_id=2836,
        industry_name='private university',
        selected_palette='default-15',
        theme_name='theme_bewise',
        website_purpose='get_leads',
        website_type='business',
    )
