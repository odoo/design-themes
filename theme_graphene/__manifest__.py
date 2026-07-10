{
    'name': 'Graphene Theme',
    'description': 'A minimalist hero opens onto a split text block, a three-column services grid, a square feature showcase, client reference tiles, a full-width parallax image and a centered FAQ — with an acid-lime, off-white and near-black palette and a geometric, technical type pairing. Structured and product-led with credibility cues / suited for technology companies, robotics, IT services, and corporate sites',
    'category': 'Theme/Corporate',
    'summary': 'Service, Corporate, Design, Technology, Robotics, Computers, IT, Blogs',
    'sequence': 110,
    'version': '2.0.0',
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/global_customizations.xml',
        'views/homepage_customizations.xml',
    ],
    'images': [
        'static/description/graphene_poster.webp',
        'static/description/graphene_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_hero_minimalist', 's_text_block_split', 's_services_grid', 's_showcase_square', 's_references_tiles', 's_parallax', 's_faq_collapse_centered'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_showcase_square'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'data_attributes': {
                'alignment': 'left',
            },
            'template_key': (
                'website_sale.dynamic_filter_template_product_public_category_default'
            ),
            'add_classes': [
                'pt96', 'pb96',
                {
                    's_dynamic_snippet_title': 'd-none',
                },
            ],
            'remove_classes': [
                's_dynamic_category_clickable_items', 'pt64', 'pb64',
                {
                    's_dynamic_snippet_title': 'd-flex',
                },
            ],
        },
    },
    'depends': ['website'],
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_graphene/static/src/js/tour.js',
        ],
    }
}
