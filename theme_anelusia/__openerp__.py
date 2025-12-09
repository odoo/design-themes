{
    'name': 'Anelusia Theme',
    'description': 'Anelusia Fashion Theme',
    'category': 'Theme/Ecommerce',
    'version': '1.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'views/layout.xml',
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
        'static/description/anelusia_description.png',
    ],
    'price': 199,
    'currency': 'EUR',
}
