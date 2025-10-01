{
    'name': 'Beauty Theme',
    'description': 'Beauty Theme - Cosmetics, Beauty, Make Up, Hairdresser',
    'category': 'Theme/Retail',
    'version': '1.0',
    'author': 'Odoo SA',
    'depends': ['theme_loftspace', 'website_animate', 'snippet_google_map'],
    'data': [
        'views/assets.xml',
        'views/images.xml',
        'views/preset.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'images': [
        'static/description/beauty_description.png',
    ],
    'price': 4,
    'currency': 'EUR',
}
