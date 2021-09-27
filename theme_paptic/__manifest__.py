{
    'name': 'Paptic Theme',
    'description': 'Clean and sharp design.',
    'category': 'Theme/Corporate',
    'summary': 'Consultancy, Design, Tech, Computers, IT, Blogs',
    'sequence': 110,
    'version': '2.1.0',
    'author': 'Odoo S.A.',
    'depends': ['website'],
    'data': [
        'data/ir_asset.xml',
        'views/images.xml',
        'views/customizations.xml',
    ],
    'images': [
        'static/description/paptic_poster.jpg',
        'static/description/paptic_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_three_columns_default_image_1': '/theme_paptic/static/src/img/pictures/s_three_columns_1.jpg',
        'website.s_three_columns_default_image_2': '/theme_paptic/static/src/img/pictures/s_three_columns_2.jpg',
        'website.s_three_columns_default_image_3': '/theme_paptic/static/src/img/pictures/s_three_columns_3.jpg',
    },
    'snippet_lists': {
        'homepage': ['s_cover', 's_image_text', 's_references', 's_three_columns', 's_comparisons', 's_call_to_action'],
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-paptic.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_paptic/static/src/js/tour.js',
        ],
    }
}
