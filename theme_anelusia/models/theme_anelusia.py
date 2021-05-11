from odoo import models


class ThemeAnelusia(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_anelusia_post_copy(self, mod):
        # Hamburger preset
        self.enable_view('website.no_autohide_menu')

        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-1')
