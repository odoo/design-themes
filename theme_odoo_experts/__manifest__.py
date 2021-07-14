{
    'name': 'Experts Theme',
    'description': 'Experts Business Theme',
    'category': 'Theme/Corporate',
    'summary': 'Advisor, Corporate, Service, Business, Finance, IT',
    'sequence': 210,
    'version': '2.1.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common', 'website_animate'],
    'data': [
        'data/ir_asset.xml',
        'views/images.xml',

        'views/snippets/s_banner.xml',
        'views/snippets/s_media_list.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_call_to_action.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_company_team.xml',
        'views/snippets/s_references.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_masonry_block.xml',
        'views/snippets/s_image_gallery.xml',
        'views/snippets/s_showcase.xml',
        'views/snippets/s_comparisons.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_features_grid.xml',
        'views/snippets/s_product_list.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_quotes_carousel.xml',

        ],
    'images': [
        'static/description/odoo_experts_description.jpg',
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
