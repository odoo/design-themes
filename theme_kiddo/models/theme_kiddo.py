from odoo import models


class ThemeKiddo(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_kiddo_post_copy(self, mod):
        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-1')
        pass
