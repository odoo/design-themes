from odoo import models


class ThemeBuzzy(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_buzzy_post_copy(self, mod):
        self.disable_view('website.template_footer_contact')
        self.enable_view('website.template_footer_minimalist')
