# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import models

from odoo import api, SUPERUSER_ID


def post_init_hook(cr, registry):
    ''' Create a new website for each theme and install the theme on it. '''
    env = api.Environment(cr, SUPERUSER_ID, {})
    IrModule = env['ir.module.module']
    themes = IrModule.search(IrModule.get_themes_domain(), order='name')
    assert len(themes) == len(env.ref('base.module_test_themes').dependencies_id)

    xmlids = []
    for theme in themes:
        website = env['website'].create({
            'name': theme.display_name,
            'theme_id': theme.id,
        })
        xmlids.append({
            'xml_id': 'test_themes.%s' % theme.display_name.replace(' ', '_'),
            'record': website,
            'noupdate': True,  # Avoid unlink on -u
        })
        theme.with_context(apply_new_theme=True)._theme_get_stream_themes()._theme_load(website)
    env['ir.model.data']._update_xmlids(xmlids)
