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
        'data/ir_asset.xml',
        'views/snippets_options.xml',
        'views/image_library.xml',

        'views/snippets/s_banner.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_call_to_action.xml',

        ],
    'images': [
        'static/description/enark_description.jpg',
        'static/description/enark_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-enark.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_enark/static/src/js/tour.js',
        ],
    }
}
