from odoo import models

class ThemeBeauty(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_beauty_post_copy(self, mod):
        # Change preset for colors
        self.enable_view('theme_common.option_colors_03_variables')

        # Change preset for fonts
        self.enable_view('website.option_font_title_06_variables')
        self.enable_view('website.option_font_body_06_variables')
        self.enable_view('website.option_font_button_06_variables')
