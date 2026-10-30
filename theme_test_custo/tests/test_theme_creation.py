# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests import HttpCase, tagged


# TODO: `test_themes` tag should not be there, runbot config should be adapted
#       to test this module too. There is a special config for the theme repo.
@tagged('post_install', '-at_install', 'test_themes')
class Crawler(HttpCase):
    def test_01_theme_customizations(self):
        theme_custo = self.env.ref('base.module_theme_test_custo')
        website = self.env.ref('base.default_website')
        website.theme_id = theme_custo.id
        self.env['theme.utils'].with_context(load_all_views=True, apply_new_theme=True)._theme_load(theme_custo, website)
        self.env['website.page'].create({
            'url': '/example',
            'view_id': website.with_context(website_id=website.id).viewref('theme_test_custo.view_example').id,
            'is_published': True,
        })
        self.start_tour(self.env["website"].get_client_action_url('/example'), "theme_customizations", login='admin')
