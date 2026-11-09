from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_evmotiv_post_copy(self, mod):
        self.enable_view('website.template_header_boxed')
        self.enable_view('theme_evmotiv.custom_footer')
        self.enable_asset('website.ripple_effect_scss')
        self.enable_asset('website.ripple_effect_js')
