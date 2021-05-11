from odoo import models


class ThemeRealEstate(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_real_estate_post_copy(self, mod):
        # Color preset
        self.enable_view('theme_common.option_colors_05_variables')
