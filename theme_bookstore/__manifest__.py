{
    'name': 'Bookstore Theme',
    'description': 'Books, Magazines, Music',
    'category': 'Theme/Retail',
    'summary': 'Books, Magazines, Literature, Musics, Media, Store',
    'sequence': 250,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common', 'website_animate'],
    'data': [
        'views/assets.xml',
        'views/images.xml',

        'views/snippets/s_title.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_product_list.xml',
        'views/snippets/s_call_to_action.xml',
    ],
    'images': [
        'static/description/bookstore_description.png',
        'static/description/bookstore_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-bookstore.odoo.com'
}
