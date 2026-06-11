{
    'name': 'Kea Theme',
    'description': 'Cover hero feeds into alternating text-and-image rows, a featured picture, color-blocked information, and a media list — with organic blob crops on the picture and media images as the visual signature, layered over wavy line and floating shape motifs. Image-and-narrative driven / suited for technology companies, IT services, computer stores, and virtual-reality product sites',
    'category': 'Theme/Technology',
    'summary': 'Technology, Tech, IT, Computers, Stores, Virtual Reality',
    'sequence': 200,
    'version': '2.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_content.xml',

        'views/snippets/s_cover.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_picture.xml',
    ],
    'images': [
        'static/description/kea_description.png',
        'static/description/kea_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_kea/static/src/img/snippets/s_cover.webp',
        'website.s_picture_default_image': '/theme_kea/static/src/img/snippets/s_picture.webp',
        'website.s_quotes_carousel_demo_image_1': '/theme_kea/static/src/img/snippets/s_quotes_carousel_1.webp',
        'website.s_quotes_carousel_demo_image_2': '/theme_kea/static/src/img/snippets/s_quotes_carousel_2.webp',
        'website.s_media_list_default_image_1': '/theme_kea/static/src/img/snippets/s_media_list_1.webp',
        'website.s_media_list_default_image_2': '/theme_kea/static/src/img/snippets/s_media_list_2.webp',
        'website.s_media_list_default_image_3': '/theme_kea/static/src/img/snippets/s_media_list_3.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_cover', 's_text_image', 's_picture', 's_image_text', 's_color_blocks_2', 's_media_list'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_cover'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'data_attributes': {
                'size': 'small',
                'columns': '2',
                'rounded': '5',
                'gap': '4',
            },
            'background': {
                'color': 'o_cc2',
                'shape': {
                    'data-oe-shape-data': '{"shape":"web_editor/Grids/04", "colors":{"c5":"o-color-1"}}',
                    'element': """<div class="o_we_shape o_web_editor_Grids_04" style="background-image: url('/web_editor/shape/web_editor/Grids/04.svg?c5=o-color-1');""",
                },
            },

            'add_classes': [
                'pt88', 'pb88',
                {
                    's_dynamic_snippet_title': 'd-none',
                },
            ],
            'remove_classes': [
                'pt64', 'pb64',
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
