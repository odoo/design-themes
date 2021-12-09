from odoo import models


class ThemeZap(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_zap_post_copy(self, mod):
        self.enable_view('website.template_header_hamburger')
        self.enable_view('website.header_navbar_pills_style')

        self.enable_view('website.template_footer_links')

        self.enable_asset('Ripple effect SCSS')
        self.enable_asset('Ripple effect JS')
