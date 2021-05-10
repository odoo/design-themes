# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, tools
from odoo.http import request


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _add_dispatch_parameters(cls, func):
        # Allow public user to use `fw` query string in test mode to ease tests
        force_website_id = request.httprequest.args.get('fw')
        if (request.registry.in_test_mode() or tools.config.options['test_enable']) and force_website_id:
            request.env['website']._force_website(force_website_id)

        super(Http, cls)._add_dispatch_parameters(func)
