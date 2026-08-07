{
    'name': 'Zenith Theme',
    'description': 'Energetic yet serene with bold condensed Anton headings and pill-shaped buttons. Best for fitness studios, yoga and pilates centers, gyms, personal training, and wellness brands. Signature: marquee bar, inline impact stats, instructor spotlight, and a membership-plan comparison. Avoid for spas or salons focused on treatments and pricing rather than memberships.',
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
