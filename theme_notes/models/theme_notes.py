from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_notes_post_copy(self, mod):
        self.enable_view('website.template_header_hamburger')
        self.enable_view('website.no_autohide_menu')
        self.enable_view('website.header_width_full')
        self.enable_view('website.template_footer_headline')
