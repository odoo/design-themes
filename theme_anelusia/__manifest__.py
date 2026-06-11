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
    'images_preview_theme': {
        'website.library_image_10': '/theme_anelusia/static/src/img/snippets/library_image_03.webp',
        'website.library_image_05': '/theme_anelusia/static/src/img/snippets/library_image_13.webp',
        'website.library_image_08': '/theme_anelusia/static/src/img/snippets/library_image_14.webp',
        'website.library_image_13': '/theme_anelusia/static/src/img/snippets/library_image_10.webp',
        'website.library_image_03': '/theme_anelusia/static/src/img/snippets/library_image_05.webp',
        'website.library_image_02': '/theme_anelusia/static/src/img/snippets/library_image_16.webp',
        'website.s_cover_default_image': '/theme_anelusia/static/src/img/snippets/s_cover.webp',
        'website.s_media_list_default_image_1': '/theme_anelusia/static/src/img/snippets/s_media_list_1.webp',
        'website.s_image_text_default_image': '/theme_anelusia/static/src/img/snippets/s_image_text.webp',
        'website.s_media_list_default_image_2': '/theme_anelusia/static/src/img/snippets/s_media_list_2.webp',
        'website.s_text_image_default_image': '/theme_anelusia/static/src/img/snippets/s_text_image.webp',
    },
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
