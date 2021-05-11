from odoo import models


class ThemeOrchid(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_orchid_post_copy(self, mod):
        # Change preset for colors
        self.enable_view('theme_common.option_colors_03_variables')
