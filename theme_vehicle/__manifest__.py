{
    'name': 'Vehicle Theme',
    'description': 'Cover hero opens onto a title block, a three-column lineup, a featured picture, key visuals, charted KPIs, and a media list, kept clean and photo-driven throughout. Image-and-stats forward with technical credibility - suited for car dealerships, motorbike retailers, tire shops, mechanics, and vehicle repair services',
    'category': 'Theme/Services',
    'summary': 'Vehicle, Cars, Motorbikes, Bikes, Tires, Transports, Repair, Mechanics, Garages, Sports, Services',
    'sequence': 300,
    'version': '2.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',
        'views/customizations.xml',
    ],
    'images': [
        'static/description/vehicle_description.webp',
        'static/description/vehicle_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_cover', 's_title', 's_three_columns', 's_picture', 's_key_images', 's_numbers_charts', 's_media_list'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_picture'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'template_key': (
                'website_sale.dynamic_filter_template_product_public_category_default'
            ),
            'data_attributes': {
                'gap': '4',
                'alignment': 'left',
            },
            'background': {
                'color': 'o_cc2',
            },
            'add_classes': [
                'pt80', 'pb88',
            ],
            'remove_classes': [
                'pt64', 'pb64',
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_vehicle/static/src/js/tour.js',
        ],
    }
}
