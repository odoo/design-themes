from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_boilerplate_post_copy(self, mod):
        if self.env['ir.module.module']._installed().get('website_sale'):
            self.enable_view('website.template_header_sales_four')
            self.env['website.assets'].make_scss_customization(
                '/website/static/src/scss/options/user_values.scss',
                {'header-template': 'sales_four'}
            )
        else:
            self.enable_view('website.template_header_hamburger')
            self.enable_view('website.no_autohide_menu')

        self.enable_view('website.template_footer_centered')
