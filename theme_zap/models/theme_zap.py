from odoo import models


class ThemeZap(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_zap_post_copy(self, mod):
        # Disable treehouse color extensions as zap does not use the
        # same colors
        self.disable_view('theme_treehouse.option_colors_05_variables')
        self.disable_view('theme_treehouse.option_colors_06_variables')
