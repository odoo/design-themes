{
    'name': 'Cobalt Theme',
    'description': 'Clean and sharp design.',
    'category': 'Theme/Corporate',
    'summary': 'Development, IT development, Design, Tech, Computers, IT, Blogs',
    'sequence': 110,
    'version': '2.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',
        'views/customizations.xml',
        'views/new_page_template.xml',
    ],
    'images': [
        'static/description/cobalt_poster.jpg',
        'static/description/cobalt_screenshot.jpg',
    ],
    'configurator_snippets': {
        'homepage': ['s_banner', 's_image_text', 's_key_images', 's_text_image', 's_company_team_detail', 's_references_grid'],
    },
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-cobalt.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_cobalt/static/src/js/tour.js',
        ],
    }
}
