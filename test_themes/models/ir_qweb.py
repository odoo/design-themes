# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models
from odoo.http import request


class IrQWeb(models.AbstractModel):
    _inherit = "ir.qweb"

    def _prepare_frontend_environment(self, values):
        irQweb = super()._prepare_frontend_environment(values)

        if 'multi_website_websites' in values:
            websites_themes = self.env['website'].get_test_themes_websites()

            for multi_website_website in values['multi_website_websites']:
                website_id = multi_website_website['website_id']
                website = websites_themes.filtered(lambda website: website.id == website_id)
                theme_img = None
                if website:
                    # prefetched by get_test_themes_websites
                    image_ids = website.theme_id.sudo().image_ids
                    if image_ids:
                        theme_img = f"<img src='/web/image/{image_ids[0].id}' width='150'/>"
                multi_website_website['theme_img'] = theme_img

        return irQweb
