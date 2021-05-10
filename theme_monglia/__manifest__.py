{
    'name': 'Monglia Theme',
    'description': 'Monglia Catering Theme',
    'category': 'Theme/Services',
    'summary': 'Restaurants, Bars, Pubs, Cafes, Catering, Food, Drinks, Concerts, Events, Shows, Musics, Dance, Party',
    'sequence': 260,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'views/assets.xml',
        'views/images_content.xml',
        'views/customizations.xml',

        'views/old_snippets/s_banner_parallax.xml',
        'views/old_snippets/s_big_icons.xml',
        'views/old_snippets/s_features_carousel.xml',
        'views/old_snippets/s_products_carousel.xml',
    ],
    'images': [
        'static/description/monglia_description.png',
        'static/description/monglia_screenshot.jpeg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-monglia.odoo.com',
}
