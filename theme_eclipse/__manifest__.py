{
    'name': 'Eclipse Theme',
    'description': 'A full-height discovery hero with large call-to-action buttons over a blurry gradient shape opens onto a client logo strip, a two-row feature grid with bordered icons, a text block paired with a doughnut chart metric, a compact quotes carousel, a line chart set against a second blurry shape, key visuals and a mobile app call-to-action, closing on a scrolling announcement ribbon backed by a third — with dark near-black palettes, off-white type and thin rules separating every section. Product-led and metric-driven / suited for SaaS products, startups, mobile apps, and technology companies',
    'category': 'Theme/Creative',
    'summary': 'Eclipse, Startup, Saas, Dark, Design, Technology, Modern, Clean, Elegant',
    'sequence': 169,
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
        'static/description/eclipse_cover.webp',
        'static/description/eclipse_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_discovery', 's_references', 's_hr', 's_features', 's_text_image', 's_quotes_carousel_compact', 's_image_text', 's_hr', 's_key_images', 's_hr', 's_cta_mobile', 's_announcement_scroll'],
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
            'theme_eclipse/static/src/js/tour.js',
        ],
    }
}
