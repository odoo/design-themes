{
    'name': 'Real Estate Theme',
    'description': 'Real Estate Theme - Houses, Appartments, Real Estate Agencies',
    'category': 'Theme/Services',
    'sequence': 320,
    'version': '1.0',
    'author': 'Odoo SA',
    'depends': ['theme_monglia', 'snippet_google_map'],
    'data': [
        'views/assets.xml',
        'views/customize_modal.xml',
        'views/images.xml',
        'views/preset.xml',
        'views/snippets.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'images': [
        'static/description/real_estate_description.png',
        'static/description/real_estate_screenshot.jpeg',
    ],
    'price': 4,
    'currency': 'EUR',
}
