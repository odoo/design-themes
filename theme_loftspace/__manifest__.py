{
    'name': 'Loftspace Theme',
    'description': 'Loftspace Fashion Theme',
    'category': 'Theme/Retail',
    'summary': 'Houses, Interiors, Decorations, Furniture, Stores',
    'sequence': 130,
    'version': '1.0',
    'depends': ['theme_common'],
    'data': [
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
        'static/description/loftspace_screenshot.jpg',
    ],
    'price': 195,
    'currency': 'EUR',
    'live_test_url': 'https://theme-loftspace.odoo.com/page/demo',
}