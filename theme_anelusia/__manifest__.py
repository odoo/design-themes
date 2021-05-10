{
    'name': 'Anelusia Theme',
    'description': 'Anelusia Fashion Theme',
    'category': 'Theme/Retail',
    'summary': 'Fashions, Trends, Clothes, Shoes, Sports, Fitness, Stores',
    'sequence': 180,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'views/assets.xml',
        'views/images_content.xml',
        'views/images_library.xml',

        'views/snippets/s_company_team.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_images_wall.xml',
        'views/snippets/s_media_list.xml',

        'views/old_snippets/s_banner_parallax.xml',
        'views/old_snippets/s_features_carousel.xml',
        'views/old_snippets/s_products_carousel.xml',
    ],
    'images': [
        'static/description/anelusia_description.png',
        'static/description/anelusia_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-anelusia.odoo.com',
}
