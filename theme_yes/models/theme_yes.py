from odoo import models

class ThemeYes(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_yes_post_copy(self, mod):
        # Change preset for fonts
        self.enable_view('website.option_font_title_02_variables')
        self.enable_view('website.option_font_body_02_variables')
        self.enable_view('website.option_font_button_02_variables')
