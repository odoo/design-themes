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
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_monglia/static/src/img/snippets/s_cover.jpg',
        'website.s_media_list_default_image_1': '/theme_monglia/static/src/img/snippets/s_media_list_1.jpg',
        'website.s_media_list_default_image_2': '/theme_monglia/static/src/img/snippets/s_media_list_2.jpg',
        'website.s_media_list_default_image_3': '/theme_monglia/static/src/img/snippets/s_media_list_3.jpg',
        'website.s_text_image_default_image': '/theme_monglia/static/src/img/snippets/s_text_image.jpg',
        'website.s_three_columns_default_image_1': '/theme_monglia/static/src/img/snippets/library_image_11.jpg',
        'website.s_three_columns_default_image_2': '/theme_monglia/static/src/img/snippets/library_image_13.jpg',
        'website.s_three_columns_default_image_3': '/theme_monglia/static/src/img/snippets/library_image_07.jpg',
        'website.library_image_03': '/theme_monglia/static/src/img/snippets/library_image_03.jpg',
        'website.library_image_10': '/theme_monglia/static/src/img/snippets/library_image_10.jpg',
        'website.library_image_13': '/theme_monglia/static/src/img/snippets/library_image_23.jpg',
        'website.library_image_02': '/theme_monglia/static/src/img/snippets/library_image_05.jpg',
        'website.library_image_14': '/theme_monglia/static/src/img/snippets/library_image_14.jpg',
        'website.library_image_16': '/theme_monglia/static/src/img/snippets/library_image_16.jpg',
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-monglia.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_monglia/static/src/js/tour.js',
        ],
    }
}
