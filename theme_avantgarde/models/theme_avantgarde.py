from odoo import models


class ThemeAvantgarde(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_avantgarde_post_copy(self, mod):
        # For compatibility
        # self.enable_asset('theme_common.compatibility_saas_10_2')

        self.disable_view('website.template_header_default')
        self.enable_view('website.template_header_magazine')
        self.enable_header_off_canvas()

        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_centered')

        self.enable_asset('website.ripple_effect_scss')
        self.enable_asset('website.ripple_effect_js')
