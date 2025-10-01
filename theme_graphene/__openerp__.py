{
    'name':'Graphene theme',
    'description': 'Light colours, thin text, clean and sharp design.',
    'category': 'Theme/Corporate',
    'version':'1.0',
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
        'demo/welcome.xml',
        'demo/style.xml',
        'demo/feat.xml',
        'demo/blocks.xml'
    ],
    'images': [
        'static/description/graphene_poster.jpg',
    ],
    'depends': ['theme_common', 'snippet_google_map', 'website_animate', 'snippet_latest_posts'],
    'price': 199,
    'currency': 'EUR',
}
