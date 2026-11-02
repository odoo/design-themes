{
    'name': 'Yes Theme',
    'description': 'Kickoff hero leads into a title block, a featured team, an image-text-overlap layout, a feature highlight, and a freegrid before a testimonial carousel and call-to-action, accented by connection and floating motifs. Image-forward and emotion-driven / suited for wedding planners, love-themed services, photographers, and personal celebration sites',
    'category': 'Theme/Personal',
    'summary': 'Wedding, Love, Photography, Services',
    'sequence': 330,
    'version': '2.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',

        'views/snippets/s_call_to_action.xml',
        'views/snippets/s_company_team.xml',
        'views/snippets/s_freegrid.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_kickoff.xml',
        'views/snippets/s_image_text_overlap.xml',
        'views/snippets/s_features.xml',
    ],
    'images': [
        'static/description/yes_description.png',
        'static/description/yes_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_kickoff', 's_title', 's_company_team', 's_image_text_overlap', 's_features', 's_freegrid', 's_quotes_carousel', 's_call_to_action'],
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
            'dynamic_snippet_args': {
                'content_data': {
                    'alignment': 'left',
                    'size': 'small',
                },
                'wrapper_data': {
                    'rounded': 2,
                    'gap': 3,
                    'size': 'small',
                },
            },
            'background': {
                'color': 'o_cc2',
            },
            'add_classes': [
                'pt32',
            ],
            'remove_classes': [
                'pb64', 'pt64',
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_yes/static/src/js/tour.js',
        ],
    }
}
