from odoo import models


class ThemeLoftspace(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_loftspace_post_copy(self, mod):
        # For compatibility
        # self.enable_asset('theme_common.compatibility_saas_10_1')
        pass
