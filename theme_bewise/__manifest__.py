{
    'name': 'Be Wise Theme',
    'description': 'Be Wise Theme',
    'category': 'Theme/Education',
    'summary': 'University, Education, Schools, Young, Play, Kids',
    'sequence': 240,
    'version': '3.0.0',
    'depends': ['theme_common'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/image_content.xml',
        'views/customizations.xml',
        'views/new_page_template.xml',
    ],
    'images': [
        'static/description/bewise_description.jpg',
        'static/description/bewise_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_picture_default_image': '/theme_bewise/static/src/img/content/college_library.jpg',
        'website.s_media_list_default_image_1': '/theme_bewise/static/src/img/content/college_media_1.jpg',
        'website.s_media_list_default_image_2': '/theme_bewise/static/src/img/content/college_media_2.jpg',
        'website.s_masonry_block_default_image_1': '/theme_bewise/static/src/img/content/content_img_25.jpg',
    },
    'configurator_snippets': {
        'homepage': ['s_striped_center_top', 's_title', 's_color_blocks_2', 's_faq_collapse', 's_masonry_block', 's_company_team_shapes'],
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-bewise.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_bewise/static/src/js/tour.js',
        ],
    }
}
