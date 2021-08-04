{
    'name': 'Odoo Experts Theme',
    'description': 'Odoo Experts Business Theme',
    'category': 'Theme/Corporate',
    'summary': 'Advisor, Corporate, Service, Business, Finance, IT',
    'sequence': 210,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'data/ir_asset.xml',
        'views/images.xml',

        'views/snippets/s_banner.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_call_to_action.xml',

        ],
    'images': [
        'static/description/odoo_experts_description.png',
        'static/description/odoo_experts_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-odoo-experts.odoo.com',
    'assets': {
        'website.assets_editor': [
            'theme_odoo_experts/static/src/js/tour.js',
        ],
    }
}
