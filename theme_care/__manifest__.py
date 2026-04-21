{
    'name': 'Care Theme',
    'description': 'Care Theme - Responsive Bootstrap Theme for Odoo CMS',
    'category': 'Theme/Creative',
    'summary': 'Care, Health, Wellness, Fitness, Gym, Yoga, Spa, Massage, Therapy ',
    'sequence': 167,
    'version': '1.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',
        'views/new_page_template.xml',

        'views/snippets/s_floating_blocks.xml',
        'views/snippets/s_splash_intro.xml',
        'views/snippets/s_masonry_block.xml',
        'views/snippets/s_reviews_wall.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_text_block.xml',
        'views/snippets/s_company_team_grid.xml',
        'views/snippets/s_cta_box.xml',
    ],
    'images': [
        'static/description/care_cover.webp',
        'static/description/care_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_care/static/src/img/snippets/s_cover.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_splash_intro', 's_text_block', 's_numbers', 's_floating_blocks', 's_company_team_grid', 's_masonry_block', 's_reviews_wall', 's_faq_collapse', 's_cta_box'],
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',

    'assets': {
        'website.assets_editor': [
            'theme_care/static/src/js/tour.js',
        ],
    }
}
