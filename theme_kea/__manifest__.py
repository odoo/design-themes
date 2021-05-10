{
    'name': 'Kea Theme',
    'description': 'Kea Theme',
    'category': 'Theme/Technology',
    'summary': 'Tech, IT, Computers, Stores',
    'sequence': 200,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'views/assets.xml',
        'views/images_content.xml',

        'views/snippets/s_cover.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_references.xml',

        'views/old_snippets/s_banner_parallax.xml',
        'views/old_snippets/s_features_carousel.xml',
    ],
    'images': [
        'static/description/kea_description.png',
        'static/description/kea_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-kea.odoo.com',
}
