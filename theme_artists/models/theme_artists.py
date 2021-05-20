from odoo import models

class ThemeArtists(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_artists_post_copy(self, mod):
        # Color preset
        self.enable_view('theme_common.option_colors_03_variables')

        # Font preset
        self.enable_view('theme_common.option_font_body_09_variables')
        self.enable_view('theme_common.option_font_title_09_variables')
        self.enable_view('theme_common.option_font_button_09_variables')
