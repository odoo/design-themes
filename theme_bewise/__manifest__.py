{
    'name': 'Be Wise Theme',
    'description': 'Spotlight intro hero with oversized heading leads into color-blocked information, a collapsible FAQ, and shape-cropped team cards, with bold geometric shape motifs accenting the team block. Information-driven / suited for universities, schools, kids education programs, and learning platforms',
    'category': 'Theme/Education',
    'summary': 'University, Education, Schools, Young, Play, Kids',
    'sequence': 240,
    'version': '3.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/image_content.xml',
        'views/customizations.xml',
    ],
    'images': [
        'static/description/bewise_description.webp',
        'static/description/bewise_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_intro_spotlight', 's_title', 's_color_blocks_2', 's_faq_collapse', 's_masonry_block_default_template', 's_company_team_shapes'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_color_blocks_2'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'dynamic_snippet_args': {
                'content_data': {
                    'size': 'small',
                },
                'wrapper_data': {
                    'rounded': 3,
                    'size': 'small',
                },
            },
            'add_classes': [
                'pt96', 'pb96',
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
            'theme_bewise/static/src/js/tour.js',
        ],
    }
}
