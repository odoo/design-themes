{
    'name': 'Monglia Theme',
    'description': 'Monglia Catering Theme',
    'category': 'Theme/Services',
    'summary': 'Event, Restaurants, Bars, Pubs, Cafes, Catering, Food, Drinks, Concerts, Shows, Musics, Dance, Party',
    'sequence': 260,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'data/ir_asset.xml',
        'views/images_content.xml',
        'views/customizations.xml',

        ],
    'images': [
        'static/description/monglia_description.png',
        'static/description/monglia_screenshot.jpeg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-monglia.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_monglia/static/src/js/tour.js',
        ],
    }
}
