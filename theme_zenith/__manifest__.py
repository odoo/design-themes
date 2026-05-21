{
    'name': 'Zenith Theme',
    'description': 'Discovery hero with a blurry shape backdrop flows into a freegrid showcase, floating image blocks, a marquee announcement bar, inline impact stats, an instructor team spotlight, a membership-plan comparison, and a collapsible FAQ, with pill-shaped buttons and bold condensed Anton headings as the typographic signature. Energy-forward yet serene / suited for fitness studios, yoga and pilates centers, gym memberships, personal training services, and wellness brands',
    'category': 'Theme/Sport',
    'summary': 'Fitness, Yoga, Pilates, Gym, Wellness, Sport, Health, Training',
    'sequence': 167,
    'version': '1.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',
        'views/global_customizations.xml',
        'views/homepage_customizations.xml',
    ],
    'images': [
        'static/description/zenith_cover.webp',
        'static/description/zenith_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_discovery', 's_freegrid', 's_title', 's_floating_blocks', 's_announcement_scroll', 's_numbers_inline', 's_company_team_spotlight', 's_comparisons', 's_faq_collapse'],
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',

    'assets': {
        'website.assets_editor': [
            'theme_zenith/static/src/js/tour.js',
        ],
    }
}
