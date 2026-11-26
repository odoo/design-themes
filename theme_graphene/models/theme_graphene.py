from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _apply_theme_config(self, module):
        if module.name != 'theme_graphene':
            return super()._apply_theme_config(module)
        self._enable_view('website.template_footer_links')
        self._enable_view('website.footer_no_copyright')
