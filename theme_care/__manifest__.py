{
    'name': 'Care Theme',
    'description': 'Banner hero leads into a story block, a numbers grid, and a color-blocked featured picture, then a detailed team grid, a masonry block with key visuals and features and a testimonials wall before a collapsible FAQ, kept clean and photo-driven without background shape decoration. Credentials-and-team driven / suited for medical clinics, dental practices, hospitals, and healthcare providers',
    'category': 'Theme/Creative',
    'summary': 'Care, Health, Wellness, Fitness, Gym, Yoga, Spa, Massage, Therapy ',
    'sequence': 10,
    'version': '1.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',

        'views/homepage_customizations.xml',
        'views/global_customizations.xml',
    ],
    'images': [
        'static/description/care_cover.webp',
        'static/description/care_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_splash_intro', 's_text_block_split', 's_numbers_lite', 's_floating_blocks', 's_company_team_grid', 's_masonry_block_quad_template', 's_reviews_wall', 's_faq_collapse', 's_cta_centered'],
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',

    'assets': {
        'website.assets_editor': [
            'theme_care/static/src/js/tour.js',
        ],
    }
}
