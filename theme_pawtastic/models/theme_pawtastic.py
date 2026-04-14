from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_pawtastic_post_copy(self, mod):
        self.enable_view("website.template_header_boxed")
        self.enable_view("website.template_footer_call_to_action")
        # Set the header as "Over The Content".
        self.set_page_option("header_overlay", True)
