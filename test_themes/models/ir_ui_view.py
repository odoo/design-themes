# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models
from odoo.http import request


class View(models.Model):
    _name = "ir.ui.view"
    _inherit = "ir.ui.view"

    @api.model
    def _prepare_qcontext(self):
        qcontext = super(View, self)._prepare_qcontext()
        if request and getattr(request, 'is_frontend', False) and 'multi_website_websites' in qcontext:
            Website = self.env['website']
            websites_themes = Website.get_test_themes_websites()

            for multi_website_website in qcontext['multi_website_websites']:
                website_id = multi_website_website['website_id']
                theme_img = None
                if website_id in websites_themes.ids:
                    # prefetched by get_test_themes_websites
                    website = Website.browse(website_id)
                    if website.theme_id.sudo().image_ids:
                        theme_img = "<img src='/web/image/%s' width='150'/>" % website.theme_id.sudo().image_ids[0].id
                multi_website_website['theme_img'] = theme_img
        return qcontext
