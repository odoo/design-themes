from odoo import models


class ThemeZap(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_zap_post_copy(self, mod):
        self.disable_view('website.template_header_default')
        self.enable_view('website.template_header_hamburger')
        self.enable_view('website.header_navbar_pills_style')

        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_links')

        self.enable_view('website.option_ripple_effect')
