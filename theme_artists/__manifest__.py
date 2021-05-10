{
    'name': 'Artists Theme',
    'description': 'Artists Theme - Art Galleries, Photography, Painting',
    'category': 'Theme/Creative',
    'summary': 'Artist, Arts, Galleries, Creative, Paintings, Photography, Shows, Stores',
    'sequence': 310,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common', 'website_animate'],
    'data': [
        'data/ir_asset.xml',
        'views/images.xml',

        'views/snippets/s_parallax.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_call_to_action.xml',

        ],
    'images': [
        'static/description/artists_description.png',
        'static/description/artists_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-artists.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_artists/static/src/js/tour.js',
        ],
    }
}
