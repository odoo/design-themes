from odoo import models

class ThemeBookstore(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_bookstore_post_copy(self, mod):
        # Change preset for fonts
        self.enable_view('website.option_font_title_05_variables')
        self.enable_view('website.option_font_body_05_variables')
        self.enable_view('website.option_font_button_05_variables')
