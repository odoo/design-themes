from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_real_estate':
            return super()._apply_theme_config(module)
        self.enable_asset("website.ripple_effect_scss")
        self.enable_asset("website.ripple_effect_js")
        self.enable_view('website.template_header_boxed')
        self.set_page_option('header_overlay', True)
        self.disable_view('website.header_call_to_action')
