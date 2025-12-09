{
    'name':'Avantgarde Theme',
    'description': 'Avantgarde is a sophisticated theme to inspire and impress',
    'category': 'Theme/Creative',
    'version':'1.1.0',
    'author':'Odoo S.A.',
    'data': [
        'views/assets.xml',
        'views/customize_modal.xml',
        'views/snippets.xml',
        'views/options.xml',
        'views/images_library.xml'
        ],
    'demo': [
        'demo/demo-data.xml',
        'demo/style.xml',
        'demo/welcome.xml',
        'demo/artgallery.xml',
        'demo/magazine.xml',
        'demo/art_shop.xml',
        'demo/blocks.xml'
    ],
    'images': [
        'static/description/poster.jpg',
    ],
    'depends': ['theme_common', 'snippet_google_map', 'snippet_latest_posts'],
    'price': 199,
    'currency': 'EUR',
}
