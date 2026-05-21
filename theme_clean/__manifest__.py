{
    'name': 'Clean Theme',
    'description': 'Vertically-rhythmic layout pairing a banner with a color-blocked section, alternating text-and-image rows, a numbers showcase, basic team block, and accordion FAQ with patterned and line image-shape crops (sketched oval ring, dot pattern, labyrinth) carrying the visual signature across the hero and content rows. Text-driven and information-dense with generous whitespace / suited for legal practices, business consultancies, technology companies, and professional services',
    'category': 'Theme/Services',
    'summary': 'Legal, Corporate, Business, Tech, Services',
    'sequence': 120,
    'version': '2.1.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/image_content.xml',

        'views/snippets/s_cta_card.xml',
        'views/snippets/s_accordion_image.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_company_team.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_numbers_showcase.xml',
    ],
    'images': [
        'static/description/clean_description.webp',
        'static/description/clean_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_image_text_default_image': '/theme_clean/static/src/img/content/image_content_20.webp',
        'website.s_banner_default_image': '/theme_clean/static/src/img/backgrounds/bg_snippet_07.webp',
        'website.s_text_image_default_image': '/theme_clean/static/src/img/content/image_content_19.webp',
        'website.s_picture_default_image': '/theme_clean/static/src/img/content/image_content_21.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_banner', 's_color_blocks_2', 's_title', 's_text_image', 's_image_text', 's_numbers_showcase', 's_company_team', 's_accordion_image', 's_cta_card'], 
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
            'dynamic_snippet_args': {
                'wrapper_data': {
                    'gap': 3,
                    'cols_count': 2,
                },
            },
            'background': {
                'shape': {
                    'data-oe-shape-data': '{"shape":"web_editor/Bold/20", "colors":{"c1":"o-color-4", "c5":"o-color-1"}}',
                    'element': """<div class="o_we_shape o_web_editor_Bold_20" style="background-image: url('/web_editor/shape/web_editor/Bold/20.svg?c1=o-color-4&c5=o-color-1');""",
                },
            },
            'add_classes': [
                'pb128',
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
            'theme_clean/static/src/js/tour.js',
        ],
    }
}
