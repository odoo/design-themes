from odoo import models


class ThemeAnelusia(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_anelusia_post_copy(self, mod):
        self.disable_view('website.template_header_default')
        self.enable_view('website.template_header_hamburger_full')
        self.enable_view('website.template_header_default_align_center')
        self.enable_view('website.template_header_hamburger_align_center')
        self.enable_view('website.no_autohide_menu')

        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_headline')

        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-1')
