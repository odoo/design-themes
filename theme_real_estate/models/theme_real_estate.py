from odoo import models


class ThemeRealEstate(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_real_estate_post_copy(self, mod):
        # For compatibility
        # self.enable_asset('theme_common.compatibility_saas_10_2')

        self.enable_asset('Ripple effect SCSS')
        self.enable_asset('Ripple effect JS')
