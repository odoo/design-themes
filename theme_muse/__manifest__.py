{
    'name': 'Muse Theme',
    'description': 'Abstract gradient hero with oversized marquee text leads into a bold editorial intro block, a references tile grid, a manifesto statement, and a minimal projects grid, then a reviews wall and a centered collapsible FAQ before a centered call-to-action, with oversized typography as the recurring visual signature. Typography-driven and minimalist / suited for design agencies, branding studios, UX/UI consultancies, and creative tech firms',
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
        'homepage': ['s_animated_cover', 's_about_bold', 's_references_tiles', 's_manifesto', 's_projects_grid_minimal', 's_reviews_wall', 's_faq_collapse_centered', 's_cta_centered'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_references_tiles'),
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',

    'assets': {
        'website.assets_editor': [
            'theme_muse/static/src/js/tour.js',
        ],
    }
}
