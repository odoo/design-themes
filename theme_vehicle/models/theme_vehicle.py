from odoo import models


class ThemeVehicle(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_vehicle_post_copy(self, mod):
        # Color preset
        self.enable_view('theme_common.option_colors_06_variables')
