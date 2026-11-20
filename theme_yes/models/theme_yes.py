from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_yes':
            return super()._apply_theme_config(module)
        self.enable_view('website.template_footer_descriptive')

        self.enable_asset("website.ripple_effect_scss")
        self.enable_asset("website.ripple_effect_js")
