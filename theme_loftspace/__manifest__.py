{
    'name': 'Loftspace Theme',
    'description': 'Loftspace Fashion Theme',
    'category': 'Theme/Retail',
    'summary': 'Houses, Interiors, Decorations, Furniture, Stores',
    'sequence': 130,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'views/assets.xml',
        'views/images_content.xml',

        'views/snippets/s_cover.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_call_to_action.xml',

        'views/old_snippets/s_banner_parallax.xml',
        'views/old_snippets/s_features_carousel.xml',
        'views/old_snippets/s_products_carousel.xml'
    ],
    'images': [
        'static/description/loftspace_description.png',
        'static/description/loftspace_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-loftspace.odoo.com',
}
