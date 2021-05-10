from odoo import models


class ThemeBeauty(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_beauty_post_copy(self, mod):
        self.disable_view('website.template_header_default')

        self.enable_view('website.template_header_contact')
        self.enable_view('website.footer_custom')
