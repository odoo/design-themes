from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_beauty':
            return super()._apply_theme_config(module)
        self.enable_view('website.footer_custom')
