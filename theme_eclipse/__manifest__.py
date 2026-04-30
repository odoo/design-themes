{
    'name': 'Eclipse Theme',
    'description': 'Eclipse Theme - Responsive Bootstrap Theme for Odoo CMS',
    'category': 'Theme/Creative',
    'summary': 'Eclipse, Startup, Saas, Dark, Design, Technology, Modern, Clean, Elegant',
    'sequence': 169,
    'version': '1.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/layout.xml',
        'views/snippets/s_hr.xml',
        'views/snippets/s_closer_look.xml',
        'views/snippets/s_references.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_quotes_carousel_compact.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_key_images.xml',
        'views/snippets/s_cta_mobile.xml',
        'views/snippets/s_announcement_scroll.xml',
    ],
    'images': [
        'static/description/eclipse_cover.webp',
        'static/description/eclipse_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_eclipse/static/src/img/snippets/s_cover.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_closer_look', 's_references', 's_hr', 's_features', 's_text_image', 's_quotes_carousel_compact', 's_image_text', 's_hr', 's_key_images', 's_hr', 's_cta_mobile', 's_announcement_scroll'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_features'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'data_attributes': {
                'gap': '3',
            },
            'add_classes': [
                'pb80',
            ],
            'remove_classes': [
                'pb64',
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',

    'assets': {
        'website.assets_editor': [
            'theme_eclipse/static/src/js/tour.js',
        ],
    }
}
