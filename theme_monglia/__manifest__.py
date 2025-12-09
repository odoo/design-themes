{
    'name': 'Monglia Theme',
    'description': 'Monglia Catering Theme',
    'category': 'Theme/Ecommerce',
    'sequence': 260,
    'version': '1.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'views/assets.xml',
        'views/customize_modal.xml',
        'views/snippets.xml',
        'views/images_content.xml',
        'views/images_library.xml',
        'views/snippet_options.xml',
    ],
    'demo': [
        'demo/demo.xml',
        'demo/blocks.xml',
        'demo/demo-menu.xml',
    ],
    'images': [
        'static/description/monglia_description.png',
        'static/description/monglia_screenshot.jpeg',
    ],
    'price': 195,
    'currency': 'EUR',
}