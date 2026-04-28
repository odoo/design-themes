# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, modules
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _match(cls, path):
        # Allow public user to use `fw` query string in test mode to ease tests
        if modules.module.current_test and (force_website_id := request.httprequest.args.get('fw')):
            request.env['website'].browse(int(force_website_id))._force()
        return super()._match(path)
