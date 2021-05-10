{
    'name': 'Anelusia Theme',
    'description': 'Anelusia Fashion Theme',
    'category': 'Theme/Retail',
    'summary': 'Diversity, Fashions, Trends, Clothes, Shoes, Sports, Fitness, Stores',
    'sequence': 180,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'data/ir_asset.xml',
        'views/images_content.xml',
        'views/images_library.xml',

        'views/snippets/s_company_team.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_images_wall.xml',
        'views/snippets/s_media_list.xml',

        ],
    'images': [
        'static/description/anelusia_description.png',
        'static/description/anelusia_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-anelusia.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_anelusia/static/src/js/tour.js',
        ],
    }
}
