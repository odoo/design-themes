from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_cobalt':
            return super()._apply_theme_config(module)
        self._enable_asset("website.ripple_effect_scss")
        self._enable_asset("website.ripple_effect_js")
        self._enable_view("website.template_header_boxed")
        self._enable_view("website.template_footer_call_to_action")
        self._enable_view("website.header_navbar_pills_style")
