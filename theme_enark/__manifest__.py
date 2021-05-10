{
    'name': 'Enark Theme',
    'description': 'Enark Theme',
    'category': 'Theme/Corporate',
    'summary': 'Corporate, Business, Finance, Services',
    'sequence': 190,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common', 'website_animate'],
    'data': [
        'views/assets.xml',
        'views/snippets_options.xml',
        'views/image_library.xml',

        'views/snippets/s_banner.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_call_to_action.xml',

        'views/old_snippets/s_big_icons.xml',
        'views/old_snippets/s_big_image.xml',
        'views/old_snippets/s_big_image_parallax.xml',
        'views/old_snippets/s_icon_box.xml',
    ],
    'images': [
        'static/description/enark_description.jpg',
        'static/description/enark_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-enark.odoo.com',
}
