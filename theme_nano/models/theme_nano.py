from odoo import models


class ThemeNano(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_nano_post_copy(self, mod):
        # Sidenav preset
        self.enable_view('website.no_autohide_menu')
