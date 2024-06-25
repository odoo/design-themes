{
    'name': 'Bookstore Theme',
    'description': 'Books, Magazines, Music',
    'category': 'Theme/Retail',
    'summary': 'Library, Books, Magazines, Literature, Musics, Media, Store',
    'sequence': 250,
    'version': '2.1.0',
    'depends': ['theme_common'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',

        'views/snippets/s_title.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_product_list.xml',
        'views/snippets/s_call_to_action.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_masonry_block.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_comparisons.xml',
        'views/snippets/s_features_grid.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/new_page_template.xml',
    ],
    'images': [
        'static/description/bookstore_description.webp',
        'static/description/bookstore_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_bookstore/static/src/img/snippets/s_cover.webp',
        'website.s_masonry_block_default_image_1': '/theme_bookstore/static/src/img/snippets/s_masonry_block.webp',
        'website.s_picture_default_image': '/theme_bookstore/static/src/img/snippets/s_picture.webp',
        'website.s_product_list_default_image_1': '/theme_bookstore/static/src/img/snippets/s_product_1.webp',
        'website.s_product_list_default_image_2': '/theme_bookstore/static/src/img/snippets/s_product_2.webp',
        'website.s_product_list_default_image_3': '/theme_bookstore/static/src/img/snippets/s_product_3.webp',
        'website.s_product_list_default_image_4': '/theme_bookstore/static/src/img/snippets/s_product_4.webp',
        'website.s_product_list_default_image_5': '/theme_bookstore/static/src/img/snippets/s_product_5.webp',
        'website.s_product_list_default_image_6': '/theme_bookstore/static/src/img/snippets/s_product_6.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_cover', 's_masonry_block', 's_image_text', 's_picture', 's_product_list', 's_call_to_action'],
    },
    'new_page_templates': {
        'about': {
            'personal': ['s_text_cover', 's_image_text', 's_text_block_h2', 's_numbers', 's_features', 's_call_to_action'],
        },
        'landing': {
            '1': ['s_banner', 's_features', 's_masonry_block', 's_call_to_action', 's_references', 's_quotes_carousel'],
            '2': ['s_cover', 's_text_image', 's_text_block_h2', 's_three_columns_landing_1', 's_call_to_action'],
            '3': ['s_text_cover', 's_text_block_h2', 's_three_columns', 's_showcase', 's_color_blocks_2', 's_quotes_carousel', 's_call_to_action'],
        },
        'services': {
            '2': ['s_text_cover', 's_image_text', 's_text_image', 's_image_text_2nd', 's_call_to_action'],
        },
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-bookstore.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_bookstore/static/src/js/tour.js',
        ],
    }
}
