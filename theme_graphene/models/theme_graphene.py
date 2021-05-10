from odoo import models


class ThemeGraphene(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_graphene_post_copy(self, mod):
        # For compatibility
        # self.enable_view('theme_common.compatibility-saas-10-2')

        self.disable_view('website.template_header_default')
        self.enable_view('website.template_header_centered_logo')
        self.enable_header_off_canvas()

        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_centered')

        self.enable_view('website.option_ripple_effect')
