from odoo import models


class ThemeKiddo(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_kiddo_post_copy(self, mod):
        self.enable_view('website.template_header_default_align_right')

        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_descriptive')

        # For compatibility
        # self.enable_asset('theme_common.compatibility_saas_10_1')
