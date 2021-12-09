from odoo import models


class ThemeYes(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_yes_post_copy(self, mod):
        self.enable_view('website.template_footer_descriptive')

        self.enable_asset('Ripple effect SCSS')
        self.enable_asset('Ripple effect JS')
