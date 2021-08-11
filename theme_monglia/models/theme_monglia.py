from odoo import models


class ThemeMonglia(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_monglia_post_copy(self, mod):
        # For compatibility
        # self.enable_asset('theme_common.compatibility_saas_10_1')

        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_minimalist')
