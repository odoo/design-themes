{
    'name': 'Be Wise Theme',
    'description': 'Be Wise Theme',
    'category': 'Theme/Education',
    'summary': 'University, Education, Schools, Young, Play, Kids',
    'sequence': 240,
    'version': '2.1.0',
    'depends': ['theme_common'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/image_content.xml',
        'views/customizations.xml',
        'views/new_page_template.xml',
    ],
    'images': [
        'static/description/bewise_description.webp',
        'static/description/bewise_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_bewise/static/src/img/backgrounds/college_bg.webp',
        'website.s_text_image_default_image': '/theme_bewise/static/src/img/content/college_graduate.webp',
        'website.s_image_text_default_image': '/theme_bewise/static/src/img/content/college_students.webp',
        'website.s_media_list_default_image_1': '/theme_bewise/static/src/img/content/college_media_1.webp',
        'website.s_media_list_default_image_2': '/theme_bewise/static/src/img/content/college_media_2.webp',
        'website.s_quotes_carousel_demo_image_0': '/theme_bewise/static/src/img/backgrounds/college_bg_4.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_cover', 's_call_to_action', 's_text_image', 's_numbers', 's_image_text', 's_quotes_carousel', 's_color_blocks_2'],
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-bewise.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_bewise/static/src/js/tour.js',
        ],
    }
}
