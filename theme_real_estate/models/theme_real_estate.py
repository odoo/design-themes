from odoo import models

class ThemeRealEstate(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_real_estate_post_copy(self, mod):
        # Color preset
        self.enable_view('theme_common.option_colors_05_variables')

        # Font preset
        self.enable_view('website.option_font_body_03_variables')
        self.enable_view('website.option_font_title_03_variables')
        self.enable_view('website.option_font_button_03_variables')
