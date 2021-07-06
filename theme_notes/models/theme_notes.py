from odoo import models


class ThemeNotes(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_notes_post_copy(self, mod):
        self.enable_header_off_canvas()

        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_descriptive')

        # For compatibility
        # self.enable_asset('theme_common.compatibility_saas_10_1')
