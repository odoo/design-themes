from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_brutalist_post_copy(self, mod):
        self.enable_view('website.template_footer_headline')
        self.disable_view('website.option_header_brand_logo')
        self.disable_view('website.header_text_element')
        self.disable_view('website.header_search_box')
        self.disable_view('website.header_call_to_action')

        self.enable_view('website.footer_no_copyright')
