from odoo import models

class ThemeGraphene(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_graphene_post_copy(self, mod):
        # Change preset for headings font
        self.enable_view('website.option_font_title_06_variables')

        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-2')
