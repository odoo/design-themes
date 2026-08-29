{
    'name': 'Notes & Play Theme',
    'description': 'Split intro pairs a full-height image with centered copy, then a client logo strip, a three-column services grid, and two full-width image-and-text rows framing a bold statement, before a detailed team block and an image-backed call-to-action. Image-forward and event-driven / suited for opera houses, orchestras, concert halls, classical ensembles, and music conservatories',
    'category': 'Theme/Retail',
    'summary': 'Opera, Classical Music, Orchestra, Symphony, Concert Hall, Philharmonic, Musicians, Live Music Venue, Theatre, Auditorium, Performances, Shows, Concerts, Events, Ticketing',
    'sequence': 30,
    'version': '2.1.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/global_customizations.xml',
        'views/homepage_customizations.xml',
    ],
    'images': [
        'static/description/notes_description.webp',
        'static/description/notes_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_split_intro', 's_references_lite', 's_services_grid', 's_hr', 's_text_image_full', 's_text_bold', 's_image_text_full', 's_company_team_detail', 's_cta_centered'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_references_lite'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'dynamic_snippet_args': {
                'wrapper_data': {
                    'cols_count': 3,
                    'gap': 4,
                    'rounded': 1,
                },
            },
            'add_classes': [
                {'s_dynamic_snippet_title': 's_dynamic_snippet_title_aside col-lg-3 flex-lg-column justify-content-lg-start'},
            ],
            'remove_classes': ['s_dynamic_category_no_arrows'],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_notes/static/src/js/tour.js',
        ],
    }
}
