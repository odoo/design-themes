{
    'name': 'Vehicle Theme',
    'description': 'Vehicle Theme - Cars, Motorbikes, Bikes, Tires',
    'category': 'Theme/Services',
    'sequence': 300,
    'version': '1.0',
    'author': 'Odoo SA',
    'depends': ['theme_monglia', 'snippet_google_map'],
    'data': [
        'views/assets.xml',
        'views/images.xml',
        'views/preset.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'images': [
        'static/description/vehicle_description.png',
        'static/description/vehicle_screenshot.jpeg',
    ],
    'price': 4,
    'currency': 'EUR',
}