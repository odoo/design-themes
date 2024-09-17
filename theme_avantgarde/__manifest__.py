{
    'name': 'Avantgarde Theme',
    'description': 'Avantgarde is a sophisticated theme to inspire and impress',
    'category': 'Theme/Creative',
    'summary': 'Design, Fine Art, Artwork, Creative, Creativity, Galleries, Trends, Shows, Magazines, Blogs',
    'sequence': 150,
    'version': '2.0.0',
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',
        'views/customizations.xml',
        'views/new_page_template.xml',
    ],
    'images': [
        'static/description/poster.jpg',
        'static/description/avantgarde_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_avantgarde/static/src/img/pictures/bg_image_08.jpg',
        'website.library_image_13': '/theme_avantgarde/static/src/img/pictures/library_image_13.jpg',
        'website.library_image_03': '/theme_avantgarde/static/src/img/pictures/library_image_03.jpg',
        'website.library_image_16': '/theme_avantgarde/static/src/img/pictures/library_image_16.jpg',
    },
    'configurator_snippets': {
        'homepage': ['s_sidegrid', 's_features_wall', 's_masonry_block', 's_carousel', 's_timeline', 's_quadrant'],
    },
    'depends': ['theme_common'],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-avantgarde.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_avantgarde/static/src/js/tour.js',
        ],
    }
}
