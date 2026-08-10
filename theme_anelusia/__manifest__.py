{
    'name': 'Anelusia Theme',
    'description': 'Shaped-container splash hero with a hamburger nav leads into a scrolling announcement strip and a fashion-category bento grid, then an e-commerce category showcase, a reviews wall, and a CTA. Image-forward and e-commerce-driven / suited for fashion, sportswear, footwear, and lifestyle retail brands',
    'category': 'Theme/Retail',
    'summary': 'Diversity, Fashions, Trends, Clothes, Shoes, Sports, Fitness, Stores',
    'sequence': 180,
    'version': '2.1.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_content.xml',
        'views/images_library.xml',

        'views/snippets/s_cta_box.xml',
        'views/snippets/s_bento_grid.xml',
        'views/snippets/s_splash_intro.xml',
        'views/snippets/s_announcement_scroll.xml',
        'views/snippets/s_ecomm_categories_showcase.xml',
        'views/snippets/s_reviews_wall.xml',
    ],
    'images': [
        'static/description/anelusia_description.webp',
        'static/description/anelusia_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_splash_intro', 's_announcement_scroll', 's_bento_grid', 's_ecomm_categories_showcase', 's_reviews_wall', 's_cta_box'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'replace', 's_ecomm_categories_showcase'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'data_attributes': {
                'rounded': '4',
                'gap': '4',
                'columns': '3',
            },
            'background': {
                'color': 'o_cc2',
            },
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_anelusia/static/src/js/tour.js',
        ],
    }
}
