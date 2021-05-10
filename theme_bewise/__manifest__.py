{
    'name': 'Be Wise Theme',
    'description': 'Be Wise Theme',
    'category': 'Theme/Education',
    'summary': 'Education, Schools, Young, Play, Kids, Sports',
    'sequence': 240,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common', 'website_animate'],
    'data': [
        'views/assets.xml',
        'views/image_content.xml',
        'views/customizations.xml',

        'views/old_snippets/s_big_icons.xml',
        'views/old_snippets/s_big_image_parallax.xml',
        'views/old_snippets/s_big_image.xml',
        'views/old_snippets/s_icon_box.xml',
    ],
    'images': [
        'static/description/bewise_description.jpg',
        'static/description/bewise_screenshot.jpeg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-bewise.odoo.com',
}
