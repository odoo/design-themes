from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_brutalist':
            return super()._apply_theme_config(module)
        self.disable_view('website.option_header_brand_logo')
        self.disable_view('website.header_text_element')
        self.disable_view('website.header_search_box')
        self.disable_view('website.header_call_to_action')

        self.enable_view('website.template_footer_headline')
        self.enable_view('website.footer_no_copyright')
