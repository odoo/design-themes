{
    'name': 'Pawtastic Theme',
    'description': 'Playful, colorful and image-forward with hand-drawn doodles, e-commerce driven. Best for pet supply stores, pet grooming, veterinary clinics, and pet care brands. Signature: colorful photo bento grid, rounded cards, numbered process steps, and trust badges.',
    'category': 'Theme/Retail',
    'summary': 'Animals, Pets, E-commerce, Safari, Nature',
    'sequence': 101,
    'version': '1.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',

        'views/global_customizations.xml',
        'views/homepage_customizations.xml',
    ],
    'images': [
        'static/description/pawtastic_cover.webp',
        'static/description/pawtastic_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_discovery', 's_freegrid', 's_image_text_overlap', 's_process_steps', 's_bento_grid', 's_reviews_wall', 's_attributes_horizontal', 's_faq_collapse'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_bento_grid'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'data_attributes': {
                'gap': '3',
                'columns': '3',
                'rounded': '5',
            },
            'background': {
                'color': 'o_cc1',
            },
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',

    'assets': {
        'website.assets_editor': [
            'theme_pawtastic/static/src/js/tour.js',
        ],
    }
}
