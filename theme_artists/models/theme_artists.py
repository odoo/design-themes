from odoo import models


class ThemeArtists(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_artists_post_copy(self, mod):
        # Color preset
        self.enable_view('theme_common.option_colors_03_variables')
