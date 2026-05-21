{
    'name': 'Bistro Theme',
    'description': 'Horizontal navigation above a full-screen image hero carrying an oversized serif wordmark, a two-column bold statement, a split cafe-style price list on a deep colored panel, a six-card review wall with star ratings, a sharp-cornered image and text box, and opening hours over a full-width dish visual. Menu-and-pricing forward with little long-form copy / suited for bistros, restaurants, bars, pubs, cafes, and catering services',
    'category': 'Theme/Food',
    'summary': 'Bistro, Restaurant, Bar, Pub, Cafe, Food, Catering',
    'sequence': 220,
    'version': '2.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/global_customizations.xml',
        'views/homepage_customizations.xml',
    ],
    'images': [
        'static/description/bistro_cover.webp',
        'static/description/bistro_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_cover', 's_about_bold', 's_pricelist_cafe', 's_reviews_wall', 's_image_text_box', 's_opening_hours_alt'],
        'pricing': ["s_text_image", "s_product_catalog"],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_pricelist_cafe'),
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
                    'gap': 3,
                    'rounded': 1,
                },
            },
            'background': {
                'color': 'o_cc2',
            },
            'add_classes': [
                'pt96', 'pb0',
            ],
            'remove_classes': [
                'pt64', 'pb64',
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_bistro/static/src/js/tour.js',
        ],
    }
}
