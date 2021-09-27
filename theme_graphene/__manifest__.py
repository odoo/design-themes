{
    'name': 'Graphene Theme',
    'description': 'Light colours, thin text, clean and sharp design.',
    'category': 'Theme/Corporate',
    'summary': 'Service, Corporate, Design, Technology, Robotics, Computers, IT, Blogs',
    'sequence': 110,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'data': [
        'data/ir_asset.xml',
        'views/images_library.xml',
        'views/customizations.xml',
    ],
    'images': [
        'static/description/graphene_poster.jpg',
        'static/description/graphene_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_graphene/static/src/img/pictures/bg_image_08.jpg',
        'website.s_text_image_default_image': '/theme_graphene/static/src/img/pictures/content_02.jpg',
        'website.s_parallax_default_image': '/theme_graphene/static/src/img/pictures/content_12.jpg',
        'website.s_picture_default_image': '/theme_graphene/static/src/img/pictures/content_04.jpg',
    },
    'snippet_lists': {
        'homepage': ['s_cover', 's_text_image', 's_numbers', 's_picture', 's_comparisons'],
    },
    'depends': ['theme_common'],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-graphene.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_graphene/static/src/js/tour.js',
        ],
    }
}
