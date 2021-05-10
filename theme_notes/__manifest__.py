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
        'views/assets.xml',
        'views/images_library.xml',

        'views/snippets/s_carousel.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_company_team.xml',

        'views/old_snippets/s_banner_parallax.xml',
        'views/old_snippets/s_features_carousel.xml',
    ],
    'images': [
        'static/description/Notes_description.png',
        'static/description/notes_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-notes.odoo.com',
}
