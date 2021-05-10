{
    'name': 'Beauty Theme',
    'description': 'Beauty Theme - Cosmetics, Beauty, Make Up, Hairdresser',
    'category': 'Theme/Retail',
    'summary': 'Health, Beauty, Care, Make Up, Cosmetics, Hair Dressers, Stores',
    'sequence': 170,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common', 'website_animate'],
    'data': [
        'views/assets.xml',
        'views/images.xml',

        'views/snippets/s_cover.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_company_team.xml',
        'views/snippets/s_call_to_action.xml',

        'views/old_snippets/s_banner_parallax.xml',
    ],
    'images': [
        'static/description/beauty_description.png',
        'static/description/beauty_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-beauty.odoo.com',
}
