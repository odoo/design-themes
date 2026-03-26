from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_care_post_copy(self, mod):
        self.enable_view('website.template_header_boxed')
        self.enable_view('website.template_footer_call_to_action')
