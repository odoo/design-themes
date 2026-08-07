{
    'name': 'Kea Theme',
    'description': 'Dark, store-driven style with a warm burnt-orange, beige and near-black palette and a signature glow. Best for technology companies, IT services, computer and electronics stores, and gadget shops. Signature: glowing hero, horizontal shopping attributes, bento grid, and opening hours. Avoid if there is no online store; this one is product and e-commerce driven. Mood: warm, cozy-dark, premium, tech-forward.',
    'category': 'Theme/Technology',
    'summary': 'Electronics, Gadgets, Devices, Tech, Technology, Store, Shop, Ecommerce',
    'sequence': 200,
    'version': '2.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_content.xml',

        'views/global_customizations.xml',
        'views/homepage_customizations.xml',
    ],
    'images': [
        'static/description/kea_description.webp',
        'static/description/kea_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_banner_glow', 's_attributes_horizontal', 's_cards_soft', 's_announcement_scroll', 's_card_offset', 's_process_steps', 's_title', 's_bento_grid', 's_opening_hours'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_attributes_horizontal'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'data_attributes': {
                'rounded': '1',
            },
            'add_classes': [
                'pt112'
            ],
            'remove_classes': [
                'pt64'
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_kea/static/src/js/tour.js',
        ],
    }
}
