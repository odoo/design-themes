from odoo import models

class ThemeClean(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_clean_post_copy(self, mod):
        # Change preset for headings font
        self.enable_view('website.option_font_title_02_variables')
