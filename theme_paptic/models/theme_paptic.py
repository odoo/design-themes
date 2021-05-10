from odoo import models


class ThemePaptic(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_paptic_post_copy(self, mod):
        # For compatibility
        # self.enable_asset('theme_common.compatibility_saas_10_2')

        self.enable_asset('website.ripple_effect_scss')
        self.enable_asset('website.ripple_effect_js')
        self.enable_view('website.template_footer_centered')
        self.enable_header_off_canvas()
