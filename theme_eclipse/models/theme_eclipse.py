from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_eclipse_post_copy(self, mod):
        self.disable_view('website.header_call_to_action')

        self.enable_view('website.template_footer_descriptive')
        self.enable_view('website.footer_no_copyright')
