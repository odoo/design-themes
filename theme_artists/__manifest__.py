{
    'name': 'Artists Theme',
    'description': 'Artists Theme - Art Galleries, Photography, Painting',
    'category': 'Theme/Creative',
    'summary': 'Arts, Galleries, Creative, Paintings, Photography, Shows, Stores',
    'sequence': 310,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common', 'website_animate'],
    'data': [
        'views/assets.xml',
        'views/images.xml',

        'views/snippets/s_parallax.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_call_to_action.xml',

        'views/old_snippets/s_banner_parallax.xml',
        'views/old_snippets/s_products_carousel.xml',
    ],
    'images': [
        'static/description/artists_description.png',
        'static/description/artists_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-artists.odoo.com',
}
