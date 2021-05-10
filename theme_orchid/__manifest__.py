{
    'name': 'Orchid Theme',
    'description': 'Orchid Theme - Flowers, Beauty',
    'category': 'Theme/Retail',
    'summary': 'Gardens, Flowers, Nature, Green, Beauty, Stores',
    'sequence': 230,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common', 'website_animate'],
    'data': [
        'views/assets.xml',
        'views/images.xml',

        'views/snippets/s_cover.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_call_to_action.xml',
    ],
    'images': [
        'static/description/orchid_description.png',
        'static/description/orchid_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-orchid.odoo.com',
}
