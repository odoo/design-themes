from odoo import models

class ThemeCommon(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_common_post_copy(self, mod):
        self.disable_view('website_theme_install.customize_modal')

        # Reset all default color and font options when switching themes
        mod = 'website'
        for nb in range(2, 19):
            if nb == 7:
                mod = 'theme_common'
            self.disable_view('%s.option_font_title_%02d_variables' % (mod, nb))
            self.disable_view('%s.option_font_body_%02d_variables' % (mod, nb))
            self.disable_view('%s.option_font_button_%02d_variables' % (mod, nb))
            self.disable_view('%s.option_font_navbar_%02d_variables' % (mod, nb))
        for nb in range(2, 9):
            self.disable_view('theme_common.option_colors_%02d_variables' % nb)

        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-11-4-variables')
        # self.enable_view('theme_common.compatibility-saas-11-4')
