from odoo import models

class ThemeAvantgarde(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_avantgarde_post_copy(self, mod):
        # Change preset for headings font
        self.enable_view('website.option_font_title_02_variables')

        # Change preset for buttons font
        self.enable_view('website.option_font_button_03_variables')

        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-2')
