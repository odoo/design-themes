{
    'name': 'Loftspace Theme',
    'description': 'Search-led header above a banner hero flows into striped intro sections, an e-commerce category showcase, a reviews wall, and a collapsible FAQ before a CTA, kept clean and photo-driven without background shape decoration. Catalog-discovery driven with social proof / suited for furniture retail, home goods stores, and lifestyle e-commerce',
    'category': 'Theme/Retail',
    'summary': 'Furniture, Toys, Games, Kids, Boys, Girls, Stores',
    'sequence': 130,
    'version': '2.1.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_content.xml',

        'views/snippets/s_cta_box.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_image_text_box.xml',
        'views/snippets/s_striped.xml',
        'views/snippets/s_text_block.xml',
        'views/snippets/s_faq_collapse.xml',
    ],
    'images': [
        'static/description/loftspace_description.webp',
        'static/description/loftspace_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_banner', 's_text_block', 's_striped', 's_title', 's_ecomm_categories_showcase', 's_image_text_box', 's_reviews_wall', 's_faq_collapse', 's_cta_box',],
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_loftspace/static/src/js/tour.js',
        ],
    }
}
