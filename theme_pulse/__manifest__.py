{
    'name': 'Pulse Theme',
    'description': 'Clean sportswear eCommerce layout pairing a three-quarter-height splash intro with a compact category grid, then alternating feature blocks, a bold statement title and a references wall. Product-first and high-contrast / suited for sportswear, activewear, fashion retail and lifestyle brands',
    'category': 'Theme/Retail',
    'summary': 'Sportswear, Activewear, Fashion, Retail, eCommerce',
    'sequence': 190,
    'version': '1.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',

        'views/global_customizations.xml',
    ],
    'images': [
        'static/description/pulse_cover.webp',
        'static/description/pulse_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_confidence', 's_features_box', 's_text_bold', 's_features_grid', 's_founder', 's_achievements_list', 's_bento_features', 's_references_tiles'],
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_pulse/static/src/js/tour.js',
        ],
    }
}
