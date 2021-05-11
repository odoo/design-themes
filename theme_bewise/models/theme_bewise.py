from odoo import models

class ThemeBewise(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_bewise_post_copy(self, mod):
        # Change preset for fonts
        self.enable_view('website.option_font_title_02_variables')
        self.enable_view('website.option_font_navbar_02_variables')
