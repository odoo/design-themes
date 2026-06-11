{
    'name': 'Bistro Theme',
    'description': 'Vertical sidebar navigation paired with an image-titled hero, key visuals, a cafe-style price list, and a testimonial carousel framed by a quadrant block, with bold geometric shapes accenting the testimonials. Menu-and-pricing forward with little long-form copy / suited for bistros, restaurants, bars, pubs, cafes, and catering services',
    'category': 'Theme/Food',
    'summary': 'Bistro, Restaurant, Bar, Pub, Cafe, Food, Catering',
    'sequence': 220,
    'version': '2.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/layout.xml',

        'views/snippets/s_image_title.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_key_images.xml',
        'views/snippets/s_quadrant.xml',

    ],
    'images': [
        'static/description/bistro_cover.webp',
        'static/description/bistro_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_bistro/static/src/img/backgrounds/17.webp',
        'website.s_media_list_default_image_1': '/theme_bistro/static/src/img/content/media_list_01.webp',
        'website.s_image_text_default_image': '/theme_bistro/static/src/img/content/image_text.webp',
        'website.s_media_list_default_image_2': '/theme_bistro/static/src/img/content/media_list_02.webp',
        'website.s_text_image_default_image': '/theme_bistro/static/src/img/content/text_image.webp',
        'website.s_quotes_carousel_demo_image_1': '/theme_bistro/static/src/img/backgrounds/s_quotes_carousel_background.webp',
        'website.library_image_10': '/theme_bistro/static/src/img/backgrounds/07.webp',
        'website.library_image_05': '/theme_bistro/static/src/img/backgrounds/11.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_image_title', 's_key_images', 's_pricelist_cafe', 's_quotes_carousel', 's_quadrant'],
        'pricing': ["s_text_image", "s_product_catalog"],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_image_title'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'data_attributes': {
                'gap': '3',
                'alignment': 'left',
            },
            'background': {
                'color': 'o_cc5',
            },
            'add_classes': [
                'pt80', 'pb112',
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
