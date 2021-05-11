from odoo import models


class ThemeLoftspaceSale(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_loftspace_sale_post_copy(self, mod):
        # FIXME not sure we should keep this
        self.enable_view('website_sale.products_add_to_cart')
        self.enable_view('website_sale.products_categories')
