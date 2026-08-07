{
    'name': 'Paptic Theme',
    'description': 'Illustration-driven with custom line art, credentials-forward. Best for consultancies, design studios, technology firms, and IT or blog-driven corporate sites. Signature: line-art illustrations as the primary visual and illustrated proof rows.',
    'category': 'Theme/Corporate',
    'summary': 'Consultancy, Design, Tech, Computers, IT, Blogs',
    'sequence': 110,
    'version': '2.1.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',
        'views/customizations.xml',
    ],
    'images': [
        'static/description/paptic_poster.webp',
        'static/description/paptic_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_cover', 's_references_lite', 's_image_text', 's_text_image', 's_masonry_block_images_template', 's_faq_list', 's_cta_box'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_image_text'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'template_key': (
                'website_sale.dynamic_filter_template_product_public_category_default'
            ),
            'data_attributes': {
                'rounded': '3',
                'gap': '3',
                'size': 'small',
                'alignment': 'left',
            },
            'remove_classes': [
                's_dynamic_category_clickable_items',
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_paptic/static/src/js/tour.js',
        ],
    }
}
