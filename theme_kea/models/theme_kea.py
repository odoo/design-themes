from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_kea_post_copy(self, mod):
        self.disable_view('website.header_call_to_action')

        self.enable_view('website.template_header_sales_one')
        self.enable_view('website.template_footer_headline')
