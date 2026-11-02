from odoo import models


class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_beauty_apply_config(self, mod):
        self.enable_view('website.footer_custom')
