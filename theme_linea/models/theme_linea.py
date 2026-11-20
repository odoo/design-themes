from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_linea':
            return super()._apply_theme_config(module)
        self.enable_view('website.template_header_hamburger')
        self.enable_view('website.no_autohide_menu')
        self.enable_view('website.template_footer_centered')

        # Set header content width to full.
        self.enable_view('website.header_width_full')
