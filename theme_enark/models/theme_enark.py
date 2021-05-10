from odoo import models


class ThemeEnark(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_enark_post_copy(self, mod):
        self.disable_view('website.template_header_default')
        self.enable_view('website.template_header_hamburger')

        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_descriptive')
