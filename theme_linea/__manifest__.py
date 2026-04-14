{
    'name': 'Linea Theme',
    'description': 'Linea Theme - Responsive Bootstrap Theme for Odoo CMS',
    'category': 'Theme/Retail',
    'summary': 'Diversity, Fashions, Trends, Clothes, Shoes, Sports, Fitness, Stores',
    'sequence': 100,
    'version': '1.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/global_customizations.xml',
        'views/homepage_customizations.xml',
    ],
    'images': [
        'static/description/linea_cover.webp',
        'static/description/linea_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_linea/static/src/img/snippets/s_cover.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_banner_product', 's_title', 's_ecomm_categories_showcase', 's_masonry_block_images_template', 's_announcement_scroll', 's_image_title', 's_references_lite', 's_opening_hours_alt'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_references_lite'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'data_attributes': {
                'gap': '4',
                'columns': '3',
                'rounded': '0',
            },
            'background': {
                'color': 'o_cc1',
            },
            'add_classes': [
                'pb32',
                'pt0',
                {
                    's_dynamic_snippet_title': 'd-none',
                    's_dynamic_snippet_container': 'container-fluid',
                },
            ],
            'remove_classes': [
                'pb64',
                'pt64',
                's_dynamic_category_no_arrows',
                {
                    's_dynamic_snippet_title': 'd-flex',
                    's_dynamic_snippet_title': 'justify-content-between',
                    's_dynamic_snippet_container': 'container',
                },
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',

    'assets': {
        'website.assets_editor': [
            'theme_linea/static/src/js/tour.js',
        ],
    }
}
