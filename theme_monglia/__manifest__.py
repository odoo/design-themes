{
    'name': 'Monglia Theme',
    'description': 'Cover hero leads into a numbers grid, a diamond-cropped team block with highlighted artist names, a freegrid showcase, image wall, and collapsible FAQ before client references, with bold geometric shape motifs accenting key sections. Event-and-showcase driven with photos and credentials cues / suited for catering services, restaurants, bars, concert venues, and event organizers',
    'category': 'Theme/Services',
    'summary': 'Event, Restaurants, Bars, Pubs, Cafes, Catering, Food, Drinks, Concerts, Shows, Musics, Dance, Party',
    'sequence': 260,
    'version': '2.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_content.xml',
        'views/customizations.xml',
    ],
    'images': [
        'static/description/monglia_description.png',
        'static/description/monglia_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_cover', 's_numbers_grid', 's_company_team_shapes', 's_text_block', 's_freegrid', 's_cta_box', 's_shape_image', 's_title', 's_images_wall', 's_faq_collapse', 's_references'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_shape_image'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'dynamic_snippet_args': {
                'wrapper_data': {
                    'rounded': 4,
                    'gap': 4,
                    'cols_count': 2,
                },
            },
            'background': {
                'color': 'o_cc4',
            },
            'add_classes': [
                'pb88',
                {
                    's_dynamic_snippet_title': 'd-none'
                },
            ],
            'remove_classes': [
                'pt64', 'pb64',
                {
                    's_dynamic_snippet_title': 'd-flex',
                },
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_monglia/static/src/js/tour.js',
        ],
    }
}
