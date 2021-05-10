from odoo import models


class ThemeArtists(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_artists_post_copy(self, mod):
        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-2')

        self.disable_view('website.template_header_default')
        self.enable_view('website.template_header_hamburger')
        self.enable_header_off_canvas()

        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_centered')

        self.enable_view('website.option_ripple_effect')
