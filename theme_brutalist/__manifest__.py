{
    'name': 'Brutalist Theme',
    'description': 'Brutalist Theme - Raw and Bold Bootstrap Theme for Odoo CMS',
    'category': 'Theme/Creative',
    'summary': 'Brutalist, Bold, Raw, Monospace, High Contrast, Modern, Minimal',
    'sequence': 170,
    'version': '1.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',

        'views/snippets/s_framed_intro.xml',
        'views/snippets/s_awards_list.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_wavy_grid.xml',
        'views/snippets/s_freegrid.xml',
        'views/snippets/s_image_punchy.xml',
    ],
    'images': [
    ],
    'images_preview_theme': {
    },
    'configurator_snippets': {
        'homepage': ['s_framed_intro', 's_awards_list', 's_title', 's_wavy_grid', 's_freegrid', 's_image_punchy'],
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
            'theme_brutalist/static/src/js/tour.js',
        ],
    }
}
