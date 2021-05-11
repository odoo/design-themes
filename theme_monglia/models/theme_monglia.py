from odoo import models


class ThemeMonglia(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_monglia_post_copy(self, mod):
        # For Hamburger preset
        self.enable_view('website.no_autohide_menu')

        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-1')
