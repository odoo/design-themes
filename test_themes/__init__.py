# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models

from odoo import api, SUPERUSER_ID


def post_init_hook(cr, registry):
    ''' Create a new website for each theme and install the theme on it. '''
    env = api.Environment(cr, SUPERUSER_ID, {})
    IrModule = env['ir.module.module']

    themes = IrModule.search([
        ('category_id', 'child_of', env.ref('base.module_category_theme').id),
    ], order='name')
    exclude_list = ['_common', '_blog', '_sale']
    themes = themes.filtered(lambda t: not any([ex for ex in exclude_list if ex in t.name]))
    assert len(themes) == len(env.ref('base.module_test_themes').dependencies_id)

    for theme in themes:
        website = env['website'].create({
            'name': theme.display_name,
            'social_facebook': 'test_themes',
            'theme_id': theme.id,
        })
        theme._theme_get_stream_themes()._theme_load(website)


def uninstall_hook(cr, registry):
    ''' Remove the created websites. '''
    env = api.Environment(cr, SUPERUSER_ID, {})
    websites_themes = env['website'].search([('social_facebook', '=', 'test_themes')])
    assert len(websites_themes) == len(env.ref('base.module_test_themes').dependencies_id)

    # Bypass foreign key constraint
    website_domain = [('website_id', 'in', websites_themes.ids)]
    env['ir.ui.view'].with_context(active_test=False, _force_unlink=True).search(website_domain).unlink()
    env['ir.attachment'].with_context(active_test=False).search(website_domain).unlink()
    websites_themes.unlink()
