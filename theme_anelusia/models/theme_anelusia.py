from odoo import models


class ThemeAnelusia(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_anelusia_post_copy(self, mod):
        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_headline')

        # For compatibility
        # self.enable_asset('theme_common.compatibility_saas_10_1')
