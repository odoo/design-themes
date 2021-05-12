# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import unittest

from odoo.tests import HttpCase, tagged


@tagged('post_install', '-at_install')
class Crawler(HttpCase):
    def test_01_crawl_every_themes(self):
        """ Crawl every website (and so every themes) to ensure all themes can
            be rendered and do not crash.
        """
        Website = self.env['website']
        websites_themes = Website.get_test_themes_websites()
        assert len(websites_themes) == len(self.env.ref('base.module_test_themes').dependencies_id)
        websites_themes_names = websites_themes.mapped('name')

        def test_crawling():
            for website in websites_themes.filtered(lambda w: w.theme_id.name != 'theme_default'):
                # Ensure theme is rendering without crashing
                r = self.url_open('/?fw=%s&debug=assets' % website.id)
                self.assertEqual(r.status_code, 200, "Ensure theme is rendering without crashing")

                # Ensure correct theme is actually loaded, see commit message
                theme_asset_url = '/web/assets/debug/%s/web.assets_frontend.css' % website.id
                self.assertTrue(theme_asset_url in r.text)
                r = self.url_open(theme_asset_url)
                self.assertTrue('/%s/static/src' % website.theme_id.name in r.text, "Ensure theme is actually loaded")
                # Ensure other website/themes are not loaded
                for name in websites_themes_names:
                    if name != website.theme_id.name:
                        self.assertFalse('/%s/static/src' % name in r.text, "Ensure other themes do not pollute current one")

        # 1. Test as public user
        test_crawling()

        # 2. Test as admin
        self.authenticate('admin', 'admin')
        test_crawling()

    # Does not work without editor fix but really useful to build the pages automatically with cr.commit()
    @unittest.skip
    def test_02_homepage_tour_every_theme(self):
        Website = self.env['website']
        websites_themes = Website.get_test_themes_websites()
        for website in websites_themes:
            self.start_tour(f"/?fw={website.id}", 'homepage', login='admin')
