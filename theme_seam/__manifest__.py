{
    'name': 'Seam Theme',
    'description': 'Intro spotlight with three staggered photos traced by a bold ribbon opens onto a row of key figures, a bento grid of commitments, a short centered statement inside a looping ribbon, a three-column projects row, a wall of frosted-glass reviews crossed by a bold line, and a call-to-action card traced by a ribbon, with thick round-capped ribbon shapes and heavy geometric headings as the recurring visual signature. Bold and graphic, project- and proof-driven / suited for audio-visual rental and installation companies, sound and stage lighting equipment suppliers, AV consultants and repair services, and home cinema installers and stores',
    'category': 'Theme/Services',
    'summary': 'Seam, Audio-Visual, Sound, Lighting, Stage, Events, Equipment, Rental, Installation, Home Cinema',
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
        'homepage': ['s_intro_spotlight', 's_numbers_lite', 's_bento_features', 's_text_bold', 's_projects_grid_minimal', 's_reviews_wall', 's_cta_centered'],
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
