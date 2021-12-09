from odoo import models


class ThemeBookstore(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_bookstore_post_copy(self, mod):
        self.enable_view('website.template_header_contact')
        self.enable_view('website.template_footer_links')

