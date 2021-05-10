{
    'name': 'Graphene Theme',
    'description': 'Light colours, thin text, clean and sharp design.',
    'category': 'Theme/Corporate',
    'summary': 'Design, Tech, Computers, IT, Blogs',
    'sequence': 110,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'data': [
        'data/ir_asset.xml',
        'views/images_library.xml',
        'views/customizations.xml',

        ],
    'images': [
        'static/description/graphene_poster.jpg',
        'static/description/graphene_screenshot.jpg',
    ],
    'depends': ['theme_common', 'website_animate'],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-graphene.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_graphene/static/src/js/tour.js',
        ],
    }
}
