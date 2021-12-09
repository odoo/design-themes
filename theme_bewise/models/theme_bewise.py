from odoo import models


class ThemeBewise(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_bewise_post_copy(self, mod):
        self.enable_view('website.template_footer_headline')

        self.enable_asset('Ripple effect SCSS')
        self.enable_asset('Ripple effect JS')
