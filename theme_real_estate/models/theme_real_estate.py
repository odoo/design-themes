from odoo import models


class ThemeRealEstate(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_real_estate_post_copy(self, mod):
        self.enable_asset('Ripple effect SCSS')
        self.enable_asset('Ripple effect JS')
