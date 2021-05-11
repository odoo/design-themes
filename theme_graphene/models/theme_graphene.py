from odoo import models


class ThemeGraphene(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_graphene_post_copy(self, mod):
        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-2')
        pass
