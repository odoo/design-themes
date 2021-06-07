{
    'name': 'Loftspace Theme',
    'description': 'Loftspace Fashion Theme',
    'category': 'Theme/Retail',
    'summary': 'Furniture, Toys, Games, Kids, Boys, Girls, Stores',
    'sequence': 130,
    'version': '2.1.0',
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
        'views/snippets/s_image_gallery.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_features_grid.xml',
        'views/snippets/s_comparisons.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_masonry_block.xml',

        ],
    'images': [
        'static/description/loftspace_description.jpg',
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
