{
    'name': 'Seam Theme',
    'description': 'An indigo intro traced by a mint ribbon, with three staggered photos, opens onto a row of key figures, a bento grid of commitments, a statement inside a bold looping ribbon, a row of recent projects, a wall of frosted customer reviews crossed by a bold line and an indigo call-to-action card traced by a mint ribbon — with blue-black pages, bright indigo sections and heavy geometric type. Bold and graphic / suited for design studios, agencies, startups and technology companies',
    'category': 'Theme/Creative',
    'summary': 'Seam, Bauhaus, Geometric, Bold, Dark, Agency, Studio, Startup, Technology',
    'sequence': 172,
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
        'static/description/seam_cover.webp',
        'static/description/seam_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_intro_spotlight', 's_numbers_lite', 's_bento_features', 's_text_bold', 's_projects_grid', 's_reviews_wall', 's_cta_centered'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_bento_features'),
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_seam/static/src/js/tour.js',
        ],
    }
}
