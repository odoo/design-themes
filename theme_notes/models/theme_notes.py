from odoo import models


class ThemeNotes(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_notes_post_copy(self, mod):
        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-1')
        pass
