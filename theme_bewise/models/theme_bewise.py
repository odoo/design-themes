from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_bewise':
            return super()._apply_theme_config(module)
        self.enable_view('website.template_footer_headline')

        self.enable_asset("website.ripple_effect_scss")
        self.enable_asset("website.ripple_effect_js")
