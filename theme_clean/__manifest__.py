{
    'name': 'Clean Theme',
    'description': 'Clean Theme',
    'category': 'Theme/Services',
    'summary': 'Legal, Corporate, Business, Tech, Services',
    'sequence': 120,
    'version': '2.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'data/ir_asset.xml',
        'views/image_content.xml',

        'views/snippets/s_cover.xml',
        'views/snippets/s_carousel.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_call_to_action.xml',
    ],
    'images': [
        'static/description/Clean_description.jpg',
        'static/description/clean_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-clean.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_clean/static/src/js/tour.js',
        ],
    }
}
