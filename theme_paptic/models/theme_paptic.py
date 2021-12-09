from odoo import models


class ThemePaptic(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_paptic_post_copy(self, mod):
        self.enable_asset('Ripple effect SCSS')
        self.enable_asset('Ripple effect JS')
        self.enable_view('website.template_footer_centered')
        self.enable_header_off_canvas()
