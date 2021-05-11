from odoo import models

class ThemeEnark(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_enark_post_copy(self, mod):
        # Change preset for headings font
        self.enable_view('website.option_font_title_02_variables')
        self.enable_view('website.option_font_navbar_02_variables')
