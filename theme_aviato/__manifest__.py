{
    'name': 'Aviato Theme',
    'description': 'Aviato Theme - Responsive Bootstrap Theme for Odoo CMS',
    'category': 'Theme/Creative',
    'summary': 'Travel, Excursion, Plane, Tour, Agency ',
    'sequence': 130,
    'version': '1.0.0',
    'depends': ['theme_common'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/snippets/s_banner.xml',
        'views/snippets/s_framed_intro.xml',
        'views/snippets/s_cards_grid.xml',
        'views/snippets/s_cta_box.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_company_team.xml',
        'views/snippets/s_comparisons_horizontal.xml',
        'views/snippets/s_striped_top.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_sidegrid.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_freegrid.xml',
        'views/snippets/s_hr.xml',
        'views/snippets/s_image_title.xml',
        'views/snippets/s_images_mosaic.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_image_punchy.xml',
        'views/snippets/s_card_offset.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_masonry_block.xml',
        'views/snippets/s_motto.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_popup.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_quotes_carousel_minimal.xml',
        'views/snippets/s_features_wall.xml',
        'views/snippets/s_striped_center_top.xml',
        'views/snippets/s_showcase.xml',
        'views/snippets/s_quadrant.xml',
        'views/snippets/s_unveil.xml',
        'views/snippets/s_accordion_image.xml',
        'views/snippets/s_key_benefits.xml',
        'views/snippets/s_carousel.xml',
        'views/snippets/s_carousel_intro.xml',
        'views/snippets/s_image_hexagonal.xml',
        'views/snippets/s_key_images.xml',
        'views/snippets/s_big_number.xml',
        'views/snippets/s_image_frame.xml',
        'views/snippets/s_wavy_grid.xml',
        'views/snippets/s_shape_image.xml',
        'views/snippets/s_images_constellation.xml',
        'views/snippets/s_text_cover.xml',
        'views/snippets/s_empowerment.xml',
        'views/snippets/s_company_team_spotlight.xml',
        'views/snippets/s_numbers_boxed.xml',
        'views/new_page_template.xml',
    ],
    'images': [
        'static/description/aviato_cover.jpg',
        'static/description/aviato_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_image_text_default_image': '/theme_aviato/static/src/img/content/s_banner_2.jpg',
        'website.s_product_list_default_image_1': '/theme_aviato/static/src/img/content/s_banner_3.jpg',
        'website.s_picture_default_image': '/theme_aviato/static/src/img/content/s_popup.jpg',
        'website.s_media_list_default_image_1': '/theme_aviato/static/src/img/content/s_wall_01.jpg',
        'website.s_carousel_default_image_1': '/theme_aviato/static/src/img/content/s_carousel_1.jpg',
        'website.s_quotes_carousel_demo_image_2': '/theme_aviato/static/src/img/content/s_quote_bg_3.jpg',
        'website.s_text_image_default_image': '/theme_aviato/static/src/img/content/s_wall_05.jpg',
        'website.s_three_columns_default_image_1': '/theme_aviato/static/src/img/content/s_three_columns_1.jpg',
        'website.s_quotes_carousel_demo_image_0': '/theme_aviato/static/src/img/content/s_quote_bg_1.jpg',
    },
    'configurator_snippets': {
        'homepage': ['s_banner', 's_text_image', 's_image_text', 's_picture', 's_title', 's_masonry_block_default_template', 's_company_team', 's_showcase', 's_quotes_carousel'],
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-aviato.odoo.com',

    'assets': {
        'website.assets_editor': [
            'theme_aviato/static/src/js/tour.js',
        ],
    }
}
