{
    'name': 'Clean Theme',
    'description': 'Clean Theme',
    'category': 'Theme/Services',
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
    ],
    'price': 199,
    'currency': 'EUR',
    'live_test_url': 'https://theme-clean.odoo.com/page/demo_page_home',
}
