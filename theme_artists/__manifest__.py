{
    'name': 'Artists Theme',
    'description': 'Artists Theme - Art Galleries, Photography, Painting',
    'category': 'Theme/Creative',
    'summary': 'Artist, Arts, Galleries, Creative, Paintings, Photography, Shows, Stores',
    'sequence': 310,
    'version': '2.1.0',
    'depends': ['theme_common'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',

        'views/snippets/s_striped_top.xml',
        'views/snippets/s_cta_box.xml',
        'views/snippets/s_parallax.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_framed_intro.xml',
        'views/snippets/s_card_offset.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_call_to_action.xml',
        'views/snippets/s_cards_grid.xml',
        'views/snippets/s_carousel.xml',
        'views/snippets/s_carousel_intro.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_image_gallery.xml',
        'views/snippets/s_image_punchy.xml',
        'views/snippets/s_sidegrid.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_image_title.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_quadrant.xml',
        'views/snippets/s_numbers_grid.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_images_mosaic.xml',
        'views/snippets/s_features_grid.xml',
        'views/snippets/s_features_wall.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_quotes_carousel_minimal.xml',
        'views/snippets/s_comparisons.xml',
        'views/snippets/s_freegrid.xml',
        'views/snippets/s_company_team.xml',
        'views/snippets/s_company_team_basic.xml',
        'views/snippets/s_product_list.xml',
        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_company_team_shapes.xml',
        'views/snippets/s_numbers_showcase.xml',
        'views/snippets/s_accordion_image.xml',
        'views/snippets/s_image_hexagonal.xml',
        'views/snippets/s_key_benefits.xml',
        'views/snippets/s_pricelist_boxed.xml',
        'views/snippets/s_striped_center_top.xml',
        'views/snippets/s_key_images.xml',
        'views/snippets/s_big_number.xml',
        'views/snippets/s_image_frame.xml',
        'views/snippets/s_wavy_grid.xml',
        'views/snippets/s_shape_image.xml',
        'views/snippets/s_text_cover.xml',
        'views/new_page_template.xml',
    ],
    'images': [
        'static/description/artists_description.jpg',
        'static/description/artists_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_carousel_default_image_1': '/theme_artists/static/src/img/snippets/s_carousel_1.jpg',
        'website.s_text_image_default_image': '/theme_artists/static/src/img/snippets/s_text_image.jpg',
        'website.s_three_columns_default_image_1': '/theme_artists/static/src/img/snippets/s_product_5.jpg',
        'website.s_three_columns_default_image_2': '/theme_artists/static/src/img/snippets/library_image_13.jpg',
        'website.s_three_columns_default_image_3': '/theme_artists/static/src/img/snippets/library_image_07.jpg',
        'website.s_cover_default_image': '/theme_artists/static/src/img/snippets/s_cover.jpg',
        'website.library_image_02': '/theme_artists/static/src/img/snippets/library_image_03.jpg',
        'website.library_image_05': '/theme_artists/static/src/img/snippets/library_image_19.jpg',
        'website.library_image_08': '/theme_artists/static/src/img/snippets/library_image_14.jpg',
        'website.library_image_10': '/theme_artists/static/src/img/snippets/library_image_10.jpg',
        'website.library_image_14': '/theme_artists/static/src/img/snippets/library_image_05.jpg',
        'website.library_image_16': '/theme_artists/static/src/img/snippets/library_image_16.jpg',
    },
    'configurator_snippets': {
        'homepage': ['s_carousel', 's_text_image', 's_three_columns', 's_title', 's_images_wall', 's_call_to_action'],
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-artists.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_artists/static/src/js/tour.js',
        ],
    }
}
