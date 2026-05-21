{
    'name': 'Buzzy Theme',
    'description': 'Illustrative banner opens onto a discovery exploration block, product showcase, key-benefit grids, and accordion-with-image FAQ, with shaped containers and organic blob motifs throughout and recurring scribble-and-marker highlights on key heading words. Content-heavy and benefit-driven, leaning illustrative rather than photo-led / suited for corporate services, technology companies, and SaaS-style product marketing sites',
    'category': 'Theme/Corporate',
    'summary': 'Corporate, Services, Technology, Shapes, Illustrations',
    'sequence': 140,
    'version': '1.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/snippets/s_cta_box.xml',
        'views/snippets/s_discovery.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_showcase.xml',
        'views/snippets/s_accordion_image.xml',
        'views/snippets/s_key_benefits.xml',
    ],
    'images': [
        'static/description/buzzy_cover.webp',
        'static/description/buzzy_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_banner', 's_discovery', 's_showcase', 's_key_benefits', 's_accordion_image', 's_cta_box'],
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
                'wrapper_data': {
                    'rounded': 3,
                    'gap': 3,
                },
            },
            'add_classes': [
                {
                    's_dynamic_snippet_title': 'd-none',
                },
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_buzzy/static/src/js/tour.js',
        ],
    }
}
