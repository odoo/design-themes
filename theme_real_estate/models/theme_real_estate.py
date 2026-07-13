from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_real_estate_post_copy(self, mod):
        self.enable_asset("website.ripple_effect_scss")
        self.enable_asset("website.ripple_effect_js")
        self.enable_view('website.template_header_boxed')
        self.set_page_option('header_overlay', True)
        self.disable_view('website.header_call_to_action')
