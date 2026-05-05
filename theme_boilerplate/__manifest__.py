{
    'name': 'Boilerplate Theme',
    'description': 'Boilerplate Theme - Responsive Bootstrap Theme for Odoo CMS',
    'category': 'Theme/Creative',
    'summary': 'Boilerplate, Startup, Redesign, Creative, Design ',
    'sequence': 167,
    'version': '1.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/snippets/s_cover.xml',
        'views/snippets/s_splash_intro.xml',
        'views/snippets/s_product_list.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_text_block.xml',
        'views/snippets/s_masonry_block.xml',
        'views/snippets/s_parallax.xml',
        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_key_images.xml',
        'views/snippets/s_reviews_wall.xml',
    ],
    'images': [
        'static/description/boilerplate_cover.webp',
        'static/description/boilerplate_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_boilerplate/static/src/img/snippets/s_cover.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_splash_intro', 's_product_list', 's_title', 's_text_block', 's_masonry_block_default_template', 's_parallax', 's_masonry_block_images_template', 's_color_blocks_2',  's_masonry_block_alternation_text_image_template', 's_key_images','s_reviews_wall'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_masonry_block'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'data_attributes': {
                'gap': '3',
            },
            'background': {
                'shape': {
                    'data-oe-shape-data': '{"shape":"web_editor/Connections/20", "colors":{"c5":"o-color-3"}}',
                    'element': """<div class="o_we_shape o_web_editor_Connections_20" style="background-image: url('/web_editor/shape/web_editor/Connections/20.svg?c5=o-color-3');""",
                },
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
            'theme_boilerplate/static/src/js/tour.js',
        ],
    }
}
