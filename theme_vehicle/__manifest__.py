{
    'name': 'Vehicle Theme',
    'description': 'Vehicle Theme - Cars, Motorbikes, Bikes, Tires',
    'category': 'Theme/Services',
    'summary': 'Vehicle, Cars, Motorbikes, Bikes, Tires, Transports, Repair, Mechanics, Garages, Sports, Services',
    'sequence': 300,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'data/ir_asset.xml',
        'views/images.xml',
        'views/customizations.xml',
    ],
    'images': [
        'static/description/vehicle_description.png',
        'static/description/vehicle_screenshot.jpeg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-vehicle.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_vehicle/static/src/js/tour.js',
        ],
    }
}
