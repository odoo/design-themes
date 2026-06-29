{
    'name': 'Notes & Play Theme',
    'description': 'Intro opens onto image-and-text storytelling, a three-column rhythm, a full image wall, and a shape-cropped team block before a strong call-to-action, with recurring underline highlights running across every section heading. Image-forward and event-driven / suited for bands, music labels, concert venues, record stores, and artist showcases',
    'category': 'Theme/Retail',
    'summary': 'Band, Musics, Sound, Concerts, Artists, Records, Event, Food, Stores',
    'sequence': 30,
    'version': '2.1.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/snippets/s_image_text.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_framed_intro.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_company_team_shapes.xml',
        'views/snippets/s_image_gallery.xml',
        'views/snippets/s_call_to_action.xml',
    ],
    'images': [
        'static/description/notes_description.webp',
        'static/description/notes_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.library_image_03': '/theme_notes/static/src/img/content/library_image_19.webp',
        'website.library_image_05': '/theme_notes/static/src/img/content/library_image_05.webp',
        'website.library_image_10': '/theme_notes/static/src/img/content/library_image_10.webp',
        'website.library_image_14': '/theme_notes/static/src/img/content/library_image_14.webp',
        'website.library_image_16': '/theme_notes/static/src/img/content/library_image_16.webp',
        'website.s_carousel_default_image_2': '/theme_notes/static/src/img/content/content_img_23.webp',
        'website.s_cover_default_image': '/theme_notes/static/src/img/content/content_img_14.webp',
        'website.s_image_text_default_image': '/theme_notes/static/src/img/content/content_img_16.webp',
        'website.s_three_columns_default_image_1': '/theme_notes/static/src/img/content/content_img_18.webp',
        'website.s_three_columns_default_image_2': '/theme_notes/static/src/img/content/content_img_19.webp',
        'website.s_three_columns_default_image_3': '/theme_notes/static/src/img/content/content_img_20.webp',
        'website.s_text_image_default_image': '/theme_notes/static/src/img/content/content_img_15.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_framed_intro', 's_image_text', 's_three_columns', 's_images_wall', 's_text_image', 's_company_team_shapes', 's_title', 's_call_to_action'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_company_team_shapes'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'data_attributes': {
                'gap': '4',
            },
            'add_classes': [
                'pb48',
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
            'theme_notes/static/src/js/tour.js',
        ],
    }
}
