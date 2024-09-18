{
    'name': 'Vehicle Theme',
    'description': 'Vehicle Theme - Cars, Motorbikes, Bikes, Tires',
    'category': 'Theme/Services',
    'summary': 'Vehicle, Cars, Motorbikes, Bikes, Tires, Transports, Repair, Mechanics, Garages, Sports, Services',
    'sequence': 300,
    'version': '2.0.0',
    'depends': ['theme_common'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',
        'views/customizations.xml',
        'views/new_page_template.xml',
    ],
    'images': [
        'static/description/vehicle_description.png',
        'static/description/vehicle_screenshot.png',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_vehicle/static/src/img/snippets/s_cover.jpg',
        'website.s_three_columns_default_image_1': '/theme_vehicle/static/src/img/snippets/s_three_columns_1.jpg',
        'website.s_three_columns_default_image_2': '/theme_vehicle/static/src/img/snippets/s_three_columns_2.jpg',
        'website.s_three_columns_default_image_3': '/theme_vehicle/static/src/img/snippets/s_three_columns_3.jpg',
        'website.s_picture_default_image': '/theme_vehicle/static/src/img/snippets/s_picture.jpg',
        'website.s_key_images_default_image_1': '/theme_vehicle/static/src/img/snippets/s_images_wall_5.jpg',
        'website.s_key_images_default_image_2': '/theme_vehicle/static/src/img/snippets/s_img_gallery_1.jpg',
        'website.s_key_images_default_image_3': '/theme_vehicle/static/src/img/snippets/s_masonry_block_2.jpg',
        'website.s_key_images_default_image_4': '/theme_vehicle/static/src/img/snippets/s_images_wall_2.jpg',
        'website.s_media_list_default_image_1': '/theme_vehicle/static/src/img/snippets/s_media_list_1.jpg',
        'website.s_media_list_default_image_2': '/theme_vehicle/static/src/img/snippets/s_media_list_2.jpg',
        'website.s_media_list_default_image_3': '/theme_vehicle/static/src/img/snippets/s_media_list_3.jpg',
    },
    'configurator_snippets': {
        'homepage': ['s_cover', 's_title', 's_three_columns', 's_picture', 's_key_images', 's_numbers_charts', 's_media_list'],
    },
    'new_page_templates': {
        'about': {
            'personal': ['s_text_cover', 's_image_text', 's_text_block_h2', 's_numbers', 's_features', 's_call_to_action'],
        },
        'team': {
            '5': ['s_text_block_h1', 's_text_block', 's_image_gallery', 's_picture'],
        },
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-vehicle.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_vehicle/static/src/js/tour.js',
        ],
    }
}
