{
    'name': 'Pawtastic Theme',
    'description': 'A search-led header above a playful hero with scribble and shape doodles leads into a colorful bento photo grid, a featured picture block, and a numbered process steps row, then a rounded-card image showcase and testimonials wall before a trust-badges strip and collapsible FAQ, with rounded-corner cards and hand-drawn doodle accents as the recurring visual signature. Image-forward and playful, e-commerce-driven / suited for pet supply stores, pet grooming services, veterinary clinics, and pet care brands',
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
            'dynamic_snippet_args': {
                'wrapper_data': {
                    'rounded': 5,
                    'gap': 3,
                    'cols_count': 3,
                },
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
