{
    'name': 'Clean Theme',
    'description': 'Clean Theme',
    'category': 'Theme/Services',
    'sequence': 120,
    'version': '1.1',
    'author': 'Odoo SA',
    'depends': ['theme_common', 'website_animate'],
    'data': [
        'views/assets.xml',
        'views/customize_modal.xml',
        'views/image_content.xml',
        'views/image_library.xml',
        'views/snippets_options.xml',
        'views/snippets.xml',
    ],
    'demo': [
        'demo/home.xml',
        'demo/blocks.xml',
    ],
    'images': [
        'static/description/Clean_description.jpg',
        'static/description/clean_screenshot.jpg',
    ],
    'price': 199,
    'currency': 'EUR',
}
