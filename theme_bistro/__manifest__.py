{
    'name': 'Bistro Theme',
    'description': 'Bistro Theme - Restaurant, Food/Drink, Catering, Food trucks',
    'category': 'Theme/Food',
    'summary': 'Restaurants, Catering, Food, Drinks, Accomodations, Lodging, Hosting, Vacations, Holidays, Travels',
    'sequence': 220,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'views/assets.xml',
        'views/images_library.xml',

        'views/snippets/s_cover.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_text_block.xml',
    ],
    'images': [
        'static/description/bistro_cover.jpg',
        'static/description/bistro_screenshot.jpeg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-bistro.odoo.com'
}
