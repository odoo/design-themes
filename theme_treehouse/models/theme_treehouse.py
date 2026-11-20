from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_treehouse':
            return super()._apply_theme_config(module)
        self.disable_view('website.header_visibility_standard')
        self.enable_view('website.header_visibility_fixed')
        self.enable_view('website.template_header_vertical')

        self.enable_view('website.template_footer_descriptive')
        self.enable_view('website.template_footer_slideout')

        self.enable_asset("website.ripple_effect_scss")
        self.enable_asset("website.ripple_effect_js")
