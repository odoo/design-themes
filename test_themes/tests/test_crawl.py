# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.tests import HttpCase, tagged


@tagged('post_install', '-at_install')
class Crawler(HttpCase):
    def test_01_crawl_every_themes(self):
        """ Crawl every website (and so every themes) to ensure all themes can
            be rendered and do not crash.
        """
        Website = self.env['website']
        websites_themes = Website.search([('social_facebook', '=', 'test_themes')])
        assert len(websites_themes) == len(self.env.ref('base.module_test_themes').dependencies_id)

        def test_crawling():
            for website in websites_themes.filtered(lambda w: w.theme_id.name != 'theme_default'):
                r = self.url_open('/?fw=%s&debug=assets' % website.id)
                self.assertEqual(r.status_code, 200, "Ensure rendering went fine as public user")
                self.assertTrue('/%s/static/src' % website.theme_id.name in r.text, "Ensure rendering went fine as public user")

        # Hack for theme_bootswatch which does not have it's own view asset
        WebsiteBootswatch = websites_themes.filtered(lambda w: w.theme_id.name == 'theme_bootswatch')
        vref = Website.with_context(website_id=WebsiteBootswatch.id).viewref
        (vref('theme_bootswatch.theme_cosmo_bs_variables') + vref('theme_bootswatch.theme_cosmo')).write({'active': True})

        # 1. Test as public user
        test_crawling()

        # 2. Test as admin
        self.authenticate('admin', 'admin')
        test_crawling()
