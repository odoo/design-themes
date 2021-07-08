{
    'name': 'Aviato',
    'description': 'Aviato Theme - Responsive Bootstrap Theme for Odoo CMS',
    'category': 'Theme/Creative',
    'summary': 'Travel, Excursion, Plane, Tour, Agency ',
    'sequence': 130,
    'version': '1.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'data/ir_asset.xml',
        'views/images_library.xml',
        
        'views/snippets/s_cover.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_popup.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_quotes_carousel.xml',
    ],
    'images': [
        'static/description/aviato_cover.jpg',
        'static/description/aviato_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-aviato.odoo.com',

    'assets': {
        'website.assets_editor': [
            'theme_aviato/static/src/js/tour.js',
        ],
    }
}
