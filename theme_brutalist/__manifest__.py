{
    'name': 'Brutalist Theme',
    'description': 'Minimal header opens onto a personal-brand hero pairing oversized serif typography with a yellow-framed portrait, then an awards list, a centered statement, and asymmetric black-and-white image grids before a full image wall and closing visual CTA, with yellow highlight accents as the recurring visual signature. Editorial and image-forward, portfolio-driven / suited for architecture firms, photographers, design studios, and personal portfolios',
    'category': 'Theme/Creative',
    'summary': 'Brutalist, Bold, Raw, Monospace, High Contrast, Modern, Minimal',
    'sequence': 170,
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
        'static/description/brutalist_description.webp',
        'static/description/brutalist_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_framed_intro', 's_awards_list', 's_title', 's_wavy_grid', 's_freegrid', 's_image_punchy'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_awards_list'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'dynamic_snippet_args': {
                'wrapper_data': {
                    'rounded': '0',
                    'gap': '3',
                }
            },
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_brutalist/static/src/js/tour.js',
        ],
    }
}
