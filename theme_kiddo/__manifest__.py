{
    'name': 'Kiddo Theme',
    'description': 'Kiddo theme for Odoo Website',
    'category': 'Theme/Retail',
    'summary': 'Nursery, Toys, Games, Kids, Boys, Girls, Stores',
    'sequence': 290,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/snippets/s_banner.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_product_list.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_call_to_action.xml',

    ],
    'images': [
        'static/description/Kiddo_description.png',
        'static/description/kiddo_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_banner_default_image': '/theme_kiddo/static/src/img/library/bg11.jpg',
        'website.s_image_text_default_image': '/theme_kiddo/static/src/img/content/content_img_14.jpg',
        'website.s_product_list_default_image_1': '/theme_kiddo/static/src/img/content/content_img_30.jpg',
        'website.s_product_list_default_image_2': '/theme_kiddo/static/src/img/content/content_img_31.jpg',
        'website.s_product_list_default_image_3': '/theme_kiddo/static/src/img/content/content_img_32.jpg',
        'website.s_product_list_default_image_4': '/theme_kiddo/static/src/img/content/content_img_33.jpg',
        'website.s_product_list_default_image_5': '/theme_kiddo/static/src/img/content/content_img_34.jpg',
        'website.s_product_list_default_image_6': '/theme_kiddo/static/src/img/content/content_img_35.jpg',
        's_three_columns_default_image_1': '/theme_kiddo/static/src/img/content/content_img_16.jpg',
        's_three_columns_default_image_2': '/theme_kiddo/static/src/img/content/content_img_17.jpg',
        's_three_columns_default_image_3': '/theme_kiddo/static/src/img/content/content_img_18.jpg',
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-kiddo.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_kiddo/static/src/js/tour.js',
        ],
    }
}
