from odoo import models


class ThemeCommon(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_common_post_copy(self, mod):
        # Reset all default color when switching themes
        self.disable_asset('Option colors 02 variables SCSS')
        self.disable_asset('Option colors 03 variables SCSS')
        self.disable_asset('Option colors 04 variables SCSS')
        self.disable_asset('Option colors 05 variables SCSS')
        self.disable_asset('Option colors 06 variables SCSS')
        self.disable_asset('Option colors 07 variables SCSS')
        self.disable_asset('Option colors 08 variables SCSS')
