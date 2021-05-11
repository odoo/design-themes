from odoo import models

class ThemeZap(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_zap_post_copy(self, mod):
        # Change font preset
        self.enable_view('website.option_font_title_02_variables')

        # Disable treehouse color and font extensions as zap does not use the
        # same colors and fonts
        self.disable_view('theme_treehouse.option_colors_05_variables')
        self.disable_view('theme_treehouse.option_colors_06_variables')
        # self.disable_view('theme_treehouse.option_font_dosis_variables') # FIXME
        self.disable_view('theme_treehouse.option_font_abel_variables')
        self.disable_view('theme_treehouse.option_font_lato_variables')
        self.disable_view('theme_treehouse.option_font_karla_variables')
        self.disable_view('theme_treehouse.option_font_laila_variables')
        self.disable_view('theme_treehouse.option_font_raleway_variables')
        self.disable_view('theme_treehouse.option_font_button_lato_variables')
        self.disable_view('theme_treehouse.option_font_title_laila_variables')
        self.disable_view('theme_treehouse.option_font_title_raleway_variables')
