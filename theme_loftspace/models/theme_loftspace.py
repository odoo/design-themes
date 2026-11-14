from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_loftspace':
            return super()._apply_theme_config(module)
        self.enable_view('website.template_header_search')
