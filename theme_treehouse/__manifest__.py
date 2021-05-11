{
    'name': 'Treehouse Theme',
    'description': 'Treehouse Theme - Responsive Bootstrap Theme for Odoo CMS',
    'category': 'Theme/Environment',
    'summary': 'Environment, Nature, Ecology, Sustainable Development, Non Profit, NGO, Travels',
    'sequence': 140,
    'version': '1.0',
    'depends': ['theme_common'],
    'data': [
        # THEME
        'views/assets.xml',
        'views/images_library.xml',
        'views/images_content.xml',
        'views/layout.xml',
        'views/snippets.xml',
        'views/snippets_options.xml',
        'views/customize_modal.xml',
        # SNIPPETS
        'views/snippets/s_panel_extended.xml',
        'views/snippets/s_share_extended.xml',
        'views/snippets/s_well_extended.xml',
    ],
    'images': [
        'static/description/treehouse_cover.jpg',
        'static/description/treehouse_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-treehouse.odoo.com/page/demo_page_01',
}
