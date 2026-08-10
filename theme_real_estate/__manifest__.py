{
    'name': 'Real Estate Theme',
    'description': 'Cover hero leads into stepped duo-panel text-and-image rows, a three-column listing layout, a team description grid, a numbers showcase, and a testimonial carousel before a call-to-action, with restrained airy styling and no recurring background shape decoration. Listing-and-trust driven / suited for real estate agencies, construction services, vacation rentals, and accommodation listings',
    'category': 'Theme/Services',
    'summary': 'Real Estate, Agencies, Construction, Services, Accomodations, Lodging, Hosting, Houses, Appartments, Vacations, Holidays, Travels',
    'sequence': 320,
    'version': '2.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',

        'views/snippets/s_cover.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_cards_soft.xml',
        'views/snippets/s_quotes_carousel.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_company_team_grid.xml',
        'views/snippets/s_numbers_showcase.xml',
        'views/snippets/s_call_to_action.xml',
    ],
    'images': [
        'static/description/real_estate_description.png',
        'static/description/real_estate_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_cover', 's_text_image', 's_image_text', 's_cards_soft', 's_title', 's_company_team_grid', 's_numbers_showcase', 's_quotes_carousel', 's_call_to_action'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_title'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'data_attributes': {
                'gap': '4',
                'rounded': '0',
                'size': 'small',
                'alignment': 'left',
            },
            'add_classes': [
                'pt96', 'pb96',
                {
                    's_dynamic_snippet_title': 'd-none',
                },
            ],
            'remove_classes': [
                'pt64', 'pb64',
                {
                    's_dynamic_snippet_title': 'd-flex',
                },
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_real_estate/static/src/js/tour.js',
        ],
    }
}
