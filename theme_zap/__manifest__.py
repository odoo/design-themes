{
    'name': 'Zap Theme',
    'description': 'Zap Theme - Corporate, Business, Marketing, Copywriting',
    'category': 'Theme/Corporate',
    'summary': 'Marketing, Copywriting, Media, Events, Non Profit, NGO, Corporate, Business, Services',
    'sequence': 160,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'views/assets.xml',
        'views/images_library.xml',

        'views/snippets/s_banner.xml',
        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_references.xml',
        'views/snippets/s_masonry_block.xml',
    ],
    'images': [
        'static/description/zap_cover.gif',
        'static/description/zap_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-zap.odoo.com'
}
