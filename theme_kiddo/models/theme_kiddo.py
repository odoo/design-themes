from odoo import models


class ThemeKiddo(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_kiddo_post_copy(self, mod):
        self.disable_view('website.template_header_default')
        self.enable_view('website.template_header_centered_logo')

        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_minimalist')

        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-1')
