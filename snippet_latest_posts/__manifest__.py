{
    'name':'Latest Posts Snippet',
    'description':'Latest Posts Snippet',
    'category': 'Website',
    'version':'1.1',
    'author':'Odoo S.A.',
    'data': [
        'views/assets.xml',
        'views/s_latest_posts.xml',
        'views/options.xml',
    ],
    'depends': ['theme_common', 'website_blog'],
    'auto_install': True,
    'images': [
        'static/description/icon.png',
    ],
}
