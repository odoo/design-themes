{
    'name': 'Buzzy Theme',
    'description': 'Illustrative and benefit-driven with organic blob motifs and scribble and marker highlights. Best for corporate services, technology companies, and SaaS-style product marketing. Signature: discovery block, product showcase, benefit grids, and accordion FAQ.',
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
            'data_attributes': {
                'gap': '3',
                'rounded': '3',
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
