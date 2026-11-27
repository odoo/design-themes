from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_zap':
            return super()._apply_theme_config(module)
        self._enable_view('website.template_header_sales_four')

        self._enable_view('website.template_footer_headline')

        self._enable_asset("website.ripple_effect_scss")
        self._enable_asset("website.ripple_effect_js")
