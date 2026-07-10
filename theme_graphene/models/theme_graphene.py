from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_graphene_post_copy(self, mod):
        self.enable_view('website.template_footer_links')
        self.enable_view('website.footer_no_copyright')
