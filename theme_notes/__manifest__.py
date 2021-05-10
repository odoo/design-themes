{
    'name': 'Notes & Play Theme',
    'description': 'Notes & Play Theme',
    'category': 'Theme/Retail',
    'summary': 'Musics, Sound, Concerts, Artists, Records, Stores',
    'sequence': 280,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/snippets/s_carousel.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_company_team.xml',

        ],
    'images': [
        'static/description/Notes_description.png',
        'static/description/notes_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-notes.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_notes/static/src/js/tour.js',
        ],
    }
}
