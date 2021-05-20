from odoo import models

class ThemeBistro(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_bistro_post_copy(self, mod):
        # Change color preset
        self.enable_view('theme_common.option_colors_05_variables')

        # Change font preset
        self.enable_view('website.option_font_body_06_variables')
        self.enable_view('website.option_font_title_06_variables')
        self.enable_view('website.option_font_button_06_variables')
