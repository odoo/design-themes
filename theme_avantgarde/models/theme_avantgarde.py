from odoo import models


class ThemeAvantgarde(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_avantgarde_post_copy(self, mod):
        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-2')
        pass
