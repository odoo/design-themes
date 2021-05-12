{
    'name': 'Nano Theme',
    'description': 'Nano Theme - Responsive Bootstrap Theme for Odoo CMS - Vertical Layout and Sidebar icons',
    'category': 'Theme/Lifestyle',
    'summary': 'Agencies, Creative, Design, IT, Services, Fancy',
    'sequence': 270,
    'version': '1.0',
    'depends': ['theme_common'],
    'data': [
        'views/assets.xml',
        'views/images_library.xml',

        'views/snippets/s_carousel.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_text_block.xml',
        'views/snippets/s_three_columns.xml',
    ],
    'images': [
        'static/description/nano_cover.gif',
        'static/description/nano_screenshot.jpeg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-nano.odoo.com/page/demo_page_01'
}
