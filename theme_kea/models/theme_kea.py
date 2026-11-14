from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_kea':
            return super()._apply_theme_config(module)
        self.disable_view('website.header_call_to_action')

        self.enable_view('website.template_header_sales_one')
        self.enable_view('website.template_footer_headline')
