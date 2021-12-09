from odoo import models


class ThemeClean(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_clean_post_copy(self, mod):
        self.enable_view('website.template_header_hamburger')
        self.enable_view('website.template_header_hamburger_align_right')
        self.enable_header_off_canvas()

        self.enable_view('website.template_footer_contact')
