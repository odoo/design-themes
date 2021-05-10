{
    'name': 'Graphene Theme',
    'description': 'Light colours, thin text, clean and sharp design.',
    'category': 'Theme/Corporate',
    'summary': 'Design, Tech, Computers, IT, Blogs',
    'sequence': 110,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'data': [
        'views/assets.xml',
        'views/images_library.xml',
        'views/customizations.xml',

        'views/old_snippets/s_showcase_slider.xml',
    ],
    'images': [
        'static/description/graphene_poster.jpg',
        'static/description/graphene_screenshot.jpg',
    ],
    'depends': ['theme_common', 'website_animate'],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-graphene.odoo.com'
}
