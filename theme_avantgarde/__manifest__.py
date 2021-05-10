{
    'name': 'Avantgarde Theme',
    'description': 'Avantgarde is a sophisticated theme to inspire and impress',
    'category': 'Theme/Creative',
    'summary': 'Arts, Galleries, Trends, Shows, Magazines, Blogs',
    'sequence': 150,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'data': [
        'views/assets.xml',
        'views/images_library.xml',
        'views/customizations.xml',

        'views/old_snippets/s_css_slider.xml',
        'views/old_snippets/s_showcase_slider.xml',
    ],
    'images': [
        'static/description/poster.jpg',
        'static/description/avantgarde_screenshot.jpg',
    ],
    'depends': ['theme_common'],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-avantgarde.odoo.com',
}
