{
    'name': 'Bookstore Theme',
    'description': 'Search-led header above a banner hero, curated key images, a title block, and accordion-with-image collapsible chapters, with heavily-rounded containers, circular image accents, and connection line motifs throughout. Catalog-discovery driven, balancing image presentation with browseable text / suited for bookstores, libraries, magazine archives, and music or media retailers',
    'category': 'Theme/Retail',
    'summary': 'Library, Books, Magazines, Literature, Musics, Media, Store',
    'sequence': 250,
    'version': '2.1.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',

        'views/global_customizations.xml',
        'views/homepage_customizations.xml',
    ],
    'images': [
        'static/description/bookstore_description.webp',
        'static/description/bookstore_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_carousel_intro', 's_bento_grid', 's_title', 's_category_and_products', 's_announcement_scroll', 's_products_and_advantages', 's_call_to_action', 's_text_bold', 's_reviews', 's_hours_and_place'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_banner'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'template_key': (
                'website_sale.dynamic_filter_template_product_public_category_default'
            ),
            'data_attributes': {
                'gap': '4',
            },
            'background': {
                'color': 'o_cc2',
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
            'theme_bookstore/static/src/js/tour.js',
        ],
    }
}
