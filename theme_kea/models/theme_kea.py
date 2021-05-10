from odoo import models


class ThemeKea(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_kea_post_copy(self, mod):
        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_call_to_action')

        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-1')
