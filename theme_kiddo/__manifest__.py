{
    'name': 'Kiddo Theme',
    'description': 'Banner hero opens onto an activities text-image section and three service-pillar columns with mixed image-shape crops (solid blob, organic-outlined frame, rounded-square), then a services icon grid and a CTA, with floating and connection line motifs across the content rows. Warm and service-storytelling driven / suited for nurseries, childcare centers, kids activity programs, and family-oriented education services',
    'category': 'Theme/Retail',
    'summary': 'Nursery, Toys, Games, Kids, Boys, Girls, Stores',
    'sequence': 290,
    'version': '2.1.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/snippets/s_banner.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_product_list.xml',
        'views/snippets/s_call_to_action.xml',
        'views/snippets/s_three_columns.xml',
    ],
    'images': [
        'static/description/kiddo_description.webp',
        'static/description/kiddo_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_banner_default_image': '/theme_kiddo/static/src/img/snippets/s_banner.webp',
        'website.s_image_text_default_image': '/theme_kiddo/static/src/img/snippets/s_image_text.webp',
        'website.s_three_columns_default_image_1': '/theme_kiddo/static/src/img/snippets/s_three_columns_default_image_1.webp',
        'website.s_three_columns_default_image_2': '/theme_kiddo/static/src/img/snippets/s_three_columns_default_image_2.webp',
        'website.s_three_columns_default_image_3': '/theme_kiddo/static/src/img/snippets/s_three_columns_default_image_3.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_banner', 's_image_text', 's_three_columns', 's_product_list', 's_call_to_action'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_banner'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'dynamic_snippet_args': {
                'content_data': {
                    'alignment': 'left',
                },
                'wrapper_data': {
                    'rounded': 4,
                    'gap': 3,
                },
            },
            'background': {
                'color': 'o_cc2',
            },
            'remove_classes': [
                's_dynamic_category_no_arrows',
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_kiddo/static/src/js/tour.js',
        ],
    }
}
