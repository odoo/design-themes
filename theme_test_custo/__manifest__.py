{
    'name': 'Custom Theme (Testing suite)',
    'summary': '',
    'description': '',
    # Remove the `/Hidden` part to make it selectable for tests purpose
    'category': 'Theme/Hidden',
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'data/images.xml',
        'data/ir_asset.xml',
        'data/menu.xml',
        'data/pages.xml',
        'data/shapes.xml',
        'views/footer.xml',
        'views/header.xml',
    ],
    'assets': {
        'web.assets_tests': [
            'theme_test_custo/static/tests/tours/**/*',
        ],
    },
    'license': 'LGPL-3',
}
