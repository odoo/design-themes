{
    'name': 'Kiddo Theme',
    'description': 'Kiddo theme for Odoo Website',
    'category': 'Theme/Retail',
    'summary': 'Toys, Games, Kids, Boys, Girls, Stores',
    'sequence': 290,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'views/assets.xml',
        'views/images_library.xml',

        'views/snippets/s_banner.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_product_list.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_call_to_action.xml',

        'views/old_snippets/s_discount.xml',
    ],
    'images': [
        'static/description/Kiddo_description.png',
        'static/description/kiddo_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-kiddo.odoo.com'
}
