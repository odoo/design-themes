{
    'name': 'Muse Theme',
    'description': 'Minimalist and typography-driven with an abstract gradient hero. Best for design agencies, branding studios, UX/UI consultancies, and creative tech firms. Signature: oversized marquee text, stacked services list, and a testimonial carousel. Avoid if you need rich photography or a product catalog; this is minimalist and typography-led. Mood: sleek, minimalist, dramatic, artistic.',
    'category': 'Theme/Creative',
    'summary': 'Design, Freelance, Creative, Technology IT, Consulting',
    'sequence': 60,
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
        'static/description/muse_cover.webp',
        'static/description/muse_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_animated_cover', 's_about_bold', 's_projects_list', 's_references_tiles', 's_manifesto', 's_quotes_carousel_compact', 's_faq_collapse'],
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',

    'assets': {
        'website.assets_editor': [
            'theme_muse/static/src/js/tour.js',
        ],
    }
}
