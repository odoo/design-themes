{
    'name': 'Loftspace Theme',
    'description': 'Loftspace Fashion Theme',
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
        # snippets
        'views/snippets/s_banner_parallax.xml',
        'views/snippets/s_banner_3.xml',
    ],
    'demo': [
        'demo/demo.xml',
        'demo/blocks.xml',
        'demo/demo-menu.xml',
    ],
    'images': [
        'static/description/loftspace_description.png',
    ],
    'price': 195,
    'currency': 'EUR',
}