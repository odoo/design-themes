{
    'name': 'Zap Theme',
    'description': 'Sales-led header above a discovery exploration block flows into key visuals, striped sections, a feature showcase, an image-titled hero, and charted KPIs before a CTA card, with bold geometric shape motifs woven across the major sections. Pitch-forward / suited for digital marketing agencies, copywriting services, media companies, and event-driven corporate sites',
    'category': 'Theme/Corporate',
    'summary': 'Digital, Marketing, Copywriting, Media, Events, Non Profit, NGO, Corporate, Business, Services',
    'sequence': 160,
    'version': '2.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/snippets/s_discovery.xml',
        'views/snippets/s_showcase.xml',
        'views/snippets/s_cta_card.xml',
        'views/snippets/s_numbers_charts.xml',
        'views/snippets/s_key_images.xml',
        'views/snippets/s_striped.xml',
        'views/snippets/s_image_title.xml',
    ],
    'images': [
        'static/description/zap_cover.gif',
        'static/description/zap_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_image_text_default_image': '/theme_zap/static/src/img/content/s_image_text.webp',
        'website.s_media_list_default_image_1': '/theme_zap/static/src/img/content/media_list_01.webp',
        'website.s_media_list_default_image_2': '/theme_zap/static/src/img/content/media_list_02.webp',
        'website.s_text_cover_default_image': '/theme_zap/static/src/img/snippets/s_cover.webp',
        'website.s_text_image_default_image': '/theme_zap/static/src/img/content/s_text_image.webp',
        'website.s_three_columns_default_image_3': '/theme_zap/static/src/img/content/three_columns_03.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_discovery', 's_key_images', 's_striped', 's_showcase', 's_image_title', 's_numbers_charts', 's_cta_card'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_striped'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'template_key': (
                'website_sale.dynamic_filter_template_product_public_category_default'
            ),
            'data_attributes': {
                'rounded': '0',
                'gap': '4',
                'alignment': 'left',
            },
            'add_classes': [
                'pt0',
                {
                    's_dynamic_snippet_title': 'd-none'
                },
            ],
            'remove_classes': [
                's_dynamic_category_clickable_items', 'pt64',
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_zap/static/src/js/tour.js',
        ],
    }
}
