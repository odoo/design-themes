from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_brutalist':
            return super()._apply_theme_config(module)
        self._disable_view('website.option_header_brand_logo')
        self._disable_view('website.header_text_element')
        self._disable_view('website.header_search_box')
        self._disable_view('website.header_call_to_action')

        self._enable_view('website.template_footer_headline')
        self._enable_view('website.footer_no_copyright')
