from odoo import models


class ThemeNotes(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_notes_post_copy(self, mod):
        self.disable_view('website.template_header_default')
        self.enable_view('website.template_header_hamburger_full')
        self.enable_view('website.template_header_hamburger_align_right')
        self.enable_header_off_canvas()

        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_descriptive')

        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-1')
