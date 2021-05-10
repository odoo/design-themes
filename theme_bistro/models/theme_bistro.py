from odoo import models


class ThemeBistro(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_bistro_post_copy(self, mod):
        self.disable_view('website.template_header_default')
        self.enable_view('website.template_header_vertical')
        self.enable_view('website.template_header_default_align_right')
        self.enable_view('website.template_header_hamburger_align_right')
        self.enable_header_off_canvas()

        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_centered')
        self.enable_view('website.template_footer_slideout')
        self.enable_view('website.option_footer_scrolltop')

        self.enable_view('website.option_ripple_effect')
