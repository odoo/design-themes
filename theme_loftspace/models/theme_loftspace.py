from odoo import models


class ThemeLoftspace(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_loftspace_post_copy(self, mod):
        self.disable_view('website.template_header_default')
        self.enable_view('website.template_header_centered_logo')

        # For compatibility
        # self.enable_asset('theme_common.compatibility_saas_10_1')
        pass
