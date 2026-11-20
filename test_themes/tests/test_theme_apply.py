# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.modules import Manifest
from odoo.tests import TransactionCase, tagged


@tagged('post_install', '-at_install')
class TestThemeApply(TransactionCase):
    """ Applying a theme already on the database is a plain ORM call.

        Module operations are forbidden inside a test, so these tests need no
        mock to prove it: were ``button_choose_theme`` to install or upgrade
        anything, they would fail on their own.

        Every theme is applied once by the ``test_themes`` post install hook,
        and rendered by ``test_crawl``. What is covered here is the flow those
        never reach: choosing a theme from a website that already has one.
    """

    def _website_using(self, theme_name):
        websites = self.env['website'].get_test_themes_websites()
        return websites.filtered(lambda w: w.theme_id.name == theme_name).ensure_one()

    def _theme_views(self, theme_name, website):
        return self.env['ir.ui.view'].with_context(active_test=False).search([
            ('key', '=like', f'{theme_name}.%'),
            ('website_id', '=', website.id),
        ])

    def test_choose_theme_already_installed(self):
        """ Choosing an installed theme applies its configuration."""
        website = self._website_using('theme_bistro')
        theme_nano = self.env.ref('base.module_theme_nano')
        Website = self.env['website'].with_context(website_id=website.id)

        # Set both views to the opposite of what theme Nano configures.
        Website.viewref('website.template_footer_descriptive').active = False
        Website.viewref('portal.footer_language_selector').active = True

        theme_nano.with_context(website_id=website.id).button_choose_theme()

        self.assertEqual(website.theme_id, theme_nano)
        self.assertTrue(
            Website.viewref('website.template_footer_descriptive').active,
            "Applying theme Nano should enable the descriptive footer.")
        self.assertFalse(
            Website.viewref('portal.footer_language_selector').active,
            "Applying theme Nano should disable the language selector.")

    def test_choose_theme_replaces_the_previous_one(self):
        """ Choosing a theme unloads the previous one and keeps the records of
            the other websites already using the new one.
        """
        website = self._website_using('theme_bistro')
        other_website = self._website_using('theme_nano')
        theme_nano = other_website.theme_id

        self.assertTrue(
            self._theme_views('theme_bistro', website),
            "The website should start with the views of theme Bistro.")
        other_views = self._theme_views('theme_nano', other_website)
        self.assertTrue(
            other_views,
            "The other website should hold the views of theme Nano.")

        theme_nano.with_context(website_id=website.id).button_choose_theme()

        self.assertEqual(website.theme_id, theme_nano)
        self.assertTrue(
            self._theme_views('theme_nano', website),
            "The views of theme Nano should have been copied on the website.")
        self.assertFalse(
            self._theme_views('theme_bistro', website),
            "The views of theme Bistro should have been unloaded.")
        self.assertEqual(
            self._theme_views('theme_nano', other_website), other_views,
            "The other website using theme Nano should keep its own views.")

    def test_addon_generation_covers_installed_themes(self):
        """ Generating the snippet templates of an addon module covers the
            snippets every installed theme declares for it.

            The theme a website will use is unknown while a module is loaded,
            and applying a theme is not a module operation, so generation
            cannot rely on a current website.
        """
        IrModule = self.env['ir.module.module']
        installed = IrModule._installed()
        themes = IrModule.search(IrModule.get_themes_domain() + [('state', '=', 'installed')])

        found = None
        for theme in themes:
            manifest = Manifest.for_addon(theme.name)
            addons = manifest and manifest.get('configurator_snippets_addons', {}) or {}
            for addon_name, pages in addons.items():
                if addon_name in installed and pages:
                    page, entries = next(iter(pages.items()))
                    found = (addon_name, page, entries[0][0])
                    break
            if found:
                break
        if not found:
            self.skipTest("No installed addon module is declared by an installed theme.")

        addon_name, page, snippet_key = found
        module, xmlid = snippet_key.split('.') if '.' in snippet_key else ('website', snippet_key)
        key = f'{module}.configurator_{page}_{xmlid}'

        View = self.env['ir.ui.view'].with_context(active_test=False)
        view = View.search([('key', '=', key)])
        self.assertTrue(view, f"{key} should have been generated for {addon_name}.")
        # Simulate the addon having been installed before the theme declared it.
        view.with_context(force_delete=True).unlink()

        addon = IrModule.search([('name', '=', addon_name)])
        self.env['theme.engine']._generate_primary_snippet_templates(addon.ids)

        self.assertTrue(
            View.search([('key', '=', key)]),
            f"Generating the templates of {addon_name} should have created {key} again.")
