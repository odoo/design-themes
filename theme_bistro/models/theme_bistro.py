from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_bistro':
            return super()._apply_theme_config(module)
        self._set_page_option('header_overlay', True)
        self._set_page_option('header_color', 'bg-black-25')
        self._set_page_option(
            'header_text_color',
            'text-o-color-5' if self.env.context.get('is_dark_palette') else 'text-o-color-4',
        )

        self._disable_view('website.option_header_brand_logo')
        self._disable_view('website.header_text_element')
        self._disable_view('website.header_call_to_action')
