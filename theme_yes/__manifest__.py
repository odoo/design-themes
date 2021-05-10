{
    'name': 'Yes Theme',
    'description': 'Yes Theme - Wedding',
    'category': 'Theme/Personal',
    'summary': 'Weddings, Love, Photography, Services',
    'sequence': 330,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common', 'website_animate'],
    'data': [
        'views/assets.xml',
        'views/images.xml',

        'views/snippets/s_carousel.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_masonry_block.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_call_to_action.xml',

        'views/old_snippets/s_banner_parallax.xml',
        'views/old_snippets/s_products_carousel.xml',
    ],
    'images': [
        'static/description/yes_description.png',
        'static/description/yes_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-yes.odoo.com',
}
