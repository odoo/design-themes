{
    'name': 'Beauty Theme',
    'description': 'Beauty Theme - Cosmetics, Beauty, Make Up, Hairdresser',
    'category': 'Theme/Retail',
    'summary': 'Beauty, Health, Care, Make Up, Cosmetics, Hair Dressers, Stores',
    'sequence': 170,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'data/ir_asset.xml',
        'views/images.xml',

        'views/snippets/s_cover.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_company_team.xml',
        'views/snippets/s_call_to_action.xml',

        ],
    'images': [
        'static/description/beauty_description.png',
        'static/description/beauty_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-beauty.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_beauty/static/src/js/tour.js',
        ],
    }
}
