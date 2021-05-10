{
    'name': 'Loftspace Theme',
    'description': 'Loftspace Fashion Theme',
    'category': 'Theme/Retail',
    'summary': 'Furniture, Toys, Games, Kids, Boys, Girls, Stores',
    'sequence': 130,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'data/ir_asset.xml',
        'views/images_content.xml',

        'views/snippets/s_cover.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_call_to_action.xml',

        ],
    'images': [
        'static/description/loftspace_description.png',
        'static/description/loftspace_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-loftspace.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_loftspace/static/src/js/tour.js',
        ],
    }
}
