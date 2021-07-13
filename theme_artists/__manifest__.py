{
    'name': 'Artists Theme',
    'description': 'Artists Theme - Art Galleries, Photography, Painting',
    'category': 'Theme/Creative',
    'summary': 'Artist, Arts, Galleries, Creative, Paintings, Photography, Shows, Stores',
    'sequence': 310,
    'version': '2.1.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common', 'website_animate'],
    'data': [
        'data/ir_asset.xml',
        'views/images.xml',

        'views/snippets/s_parallax.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_call_to_action.xml',
        'views/snippets/s_carousel.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_image_gallery.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_features_grid.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_comparisons.xml',
        'views/snippets/s_company_team.xml',
        'views/snippets/s_product_list.xml',
        'views/snippets/s_process_steps.xml',
        'views/snippets/s_color_blocks_2.xml',

        ],
    'images': [
        'static/description/artists_description.jpg',
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
