from odoo import models


class ThemeAvantgarde(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_avantgarde_post_copy(self, mod):
        # For compatibility
        # self.enable_asset('theme_common.compatibility_saas_10_2')

        self.disable_view('website.template_header_default')
        self.enable_view('website.template_header_hamburger')
        self.enable_view('website.template_header_default_align_right')
        self.enable_view('website.template_header_hamburger_align_right')

        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_descriptive')

