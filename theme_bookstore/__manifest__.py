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

        'views/snippets/s_cta_box.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_key_images.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_accordion_image.xml',
    ],
    'images': [
        'static/description/bookstore_description.webp',
        'static/description/bookstore_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_product_list_default_image_1': '/theme_bookstore/static/src/img/snippets/s_product_1.webp',
        'website.s_image_text_default_image': '/theme_bookstore/static/src/img/snippets/s_image_text.webp',
        'website.library_image_02': '/theme_bookstore/static/src/img/snippets/library_image_02.webp',
        'website.s_cover_default_image': '/theme_bookstore/static/src/img/snippets/s_cover.webp',
        'website.s_media_list_default_image_1': '/theme_bookstore/static/src/img/snippets/s_media_list_1.webp',
        'website.s_media_list_default_image_2': '/theme_bookstore/static/src/img/snippets/s_media_list_2.webp',
        'website.s_text_image_default_image': '/theme_bookstore/static/src/img/snippets/s_text_image.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_banner', 's_key_images', 's_title', 's_accordion_image', 's_cta_box'],
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
