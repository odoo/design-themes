{
    'name': 'Aviato Theme',
    'description': 'Contained banner hero opens onto a centered text intro, a free-form image grid, and a split title introducing a full image wall, then a square-icon feature showcase and a reviews wall before an image-backed call-to-action, with light serif headings and a rounded boxed header as the recurring visual signature. Narrative and image-forward / suited for travel agencies, tour operators, excursion booking, and destination marketing sites',
    'category': 'Theme/Creative',
    'summary': 'Travel, Excursion, Plane, Tour, Agency ',
    'sequence': 20,
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
        'static/description/aviato_cover.webp',
        'static/description/aviato_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_banner_contained', 's_text_block_split', 's_freegrid', 's_title_split', 's_images_wall', 's_showcase_square', 's_reviews_wall', 's_cta_centered'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_freegrid'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'dynamic_snippet_args': {
                'wrapper_data': {
                    'gap': 3,
                },
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
            'theme_aviato/static/src/js/tour.js',
        ],
    }
}
