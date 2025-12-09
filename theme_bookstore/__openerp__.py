{
    'name': 'Bookstore Theme',
    'description': 'Books, Magazines, Music',
    'category': 'Theme/Services',
    'version': '1.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_loftspace', 'website_animate'],
    'data': [
        'views/assets.xml',
        'views/images.xml',
        'views/preset.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'images': [
        'static/description/bookstore_description.png',
    ],
    'price': 4,
    'currency': 'EUR',
}