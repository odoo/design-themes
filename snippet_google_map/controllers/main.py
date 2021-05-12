# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json

from odoo import http
from odoo.http import request


class SnipperGoogleMap(http.Controller):
    @http.route('/website/google_maps_api_key', type='json', auth='public', website=True)
    def google_maps_api_key(self, **post):
        google_maps_api_key = request.env['ir.config_parameter'].sudo().get_param('google_maps_api_key')
        data = {
            'google_maps_api_key': google_maps_api_key or ''
        }
        return json.dumps(data)
