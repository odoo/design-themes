from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_pawtastic':
            return super()._apply_theme_config(module)
        self.enable_view("website.template_header_boxed")
        self.enable_view("website.template_footer_call_to_action")
        # Set the header as "Over The Content".
        self.set_page_option("header_overlay", True)
