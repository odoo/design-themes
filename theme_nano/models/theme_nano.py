from odoo import models


class ThemeNano(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_nano_post_copy(self, mod):
        self.disable_view('website.template_header_default')
        self.enable_view('website.template_header_sidebar')
        self.enable_view('website.no_autohide_menu')
        self.enable_header_off_canvas()
        self.enable_view('website.header_navbar_pills_style')

        self.disable_view('website.footer_custom')
        self.disable_view('website.template_footer_contact')  # Old theme_treehouse dependency
        self.enable_view('website.template_footer_minimalist')
        self.enable_view('website.template_footer_slideout')
        self.enable_view('website.option_footer_scrolltop')

        self.enable_view('website.option_ripple_effect')

        self.disable_view('portal.footer_language_selector')
