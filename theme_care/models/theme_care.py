from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_care':
            return super()._apply_theme_config(module)
        self._enable_view('website.template_header_boxed')
        self._set_page_option('header_overlay', True)
        self._enable_view('website.template_footer_call_to_action')
