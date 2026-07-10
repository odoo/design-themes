from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_bistro_post_copy(self, mod):
        self.set_page_option('header_overlay', True)
        self.set_page_option('header_color', 'bg-black-25')
        self.set_page_option('header_text_color', 'text-o-color-4')

        self.disable_view('website.option_header_brand_logo')
        self.disable_view('website.header_text_element')
        self.disable_view('website.header_call_to_action')
