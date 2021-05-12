from odoo import models


class ThemePaptic(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_paptic_post_copy(self, mod):
        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-2')

        self.enable_view('website.option_ripple_effect')
        self.enable_view('website.template_footer_centered')
        self.enable_header_off_canvas()
