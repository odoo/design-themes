from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_treehouse':
            return super()._apply_theme_config(module)
        self._disable_view('website.header_visibility_standard')
        self._enable_view('website.header_visibility_fixed')
        self._enable_view('website.template_header_vertical')

        self._enable_view('website.template_footer_descriptive')
        self._enable_view('website.template_footer_slideout')

        self._enable_asset("website.ripple_effect_scss")
        self._enable_asset("website.ripple_effect_js")
