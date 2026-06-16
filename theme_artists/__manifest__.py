{
    'name': 'Artists Theme',
    'description': 'Vertical sidebar navigation flanks an asymmetric side-grid layout, building toward image walls and gallery-style catalogs through framed and shape-cropped artwork. Image-forward with sparse copy / suited for art galleries, photographers, painters, and creative shows',
    'category': 'Theme/Creative',
    'summary': 'Artist, Arts, Galleries, Creative, Paintings, Photography, Shows, Stores',
    'sequence': 40,
    'version': '2.1.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',

        'views/snippets/s_cta_box.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_sidegrid.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_image_frame.xml',
        'views/snippets/s_image_gallery.xml',
        'views/snippets/s_shape_image.xml',
    ],
    'images': [
        'static/description/artists_description.webp',
        'static/description/artists_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.library_image_02': '/theme_artists/static/src/img/snippets/library_image_02.webp',
        'website.library_image_03': '/theme_artists/static/src/img/snippets/s_text_image.webp',
        'website.library_image_05': '/theme_artists/static/src/img/snippets/library_image_08.webp',
        'website.library_image_10': '/theme_artists/static/src/img/snippets/s_banner_2.webp',
        'website.library_image_13': '/theme_artists/static/src/img/snippets/s_banner.webp',
        'website.s_carousel_default_image_2': '/theme_artists/static/src/img/snippets/s_cover.webp',
        'website.library_image_14': '/theme_artists/static/src/img/snippets/library_image_14.webp',
        'website.library_image_16': '/theme_artists/static/src/img/snippets/library_image_16.webp',
        'website.s_image_text_default_image': '/theme_artists/static/src/img/snippets/s_shape_image_default_image.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_sidegrid', 's_product_catalog', 's_cta_box', 's_title', 's_image_frame', 's_images_wall', 's_shape_image'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_sidegrid'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'template_key': (
                'website_sale.dynamic_filter_template_product_public_category_default'
            ),
            'data_attributes': {
                'rounded': '0',
            },
            'background': {
                'color': 'o_cc5',
            },
            'add_classes': [
                'pb104',
            ],
            'remove_classes': [
                's_dynamic_category_clickable_items', 'pb64',
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_artists/static/src/js/tour.js',
        ],
    }
}
