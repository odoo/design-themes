{
    'name': 'Real Estate Theme',
    'description': 'Real Estate Theme - Houses, Appartments, Real Estate Agencies',
    'category': 'Theme/Services',
    'summary': 'Real Estate, Agencies, Construction, Services, Accomodations, Lodging, Hosting, Houses, Appartments, Vacations, Holidays, Travels',
    'sequence': 320,
    'version': '2.0.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_common'],
    'data': [
        'views/assets.xml',
        'views/images.xml',

        'views/snippets/s_banner.xml',
        'views/snippets/s_picture.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_three_columns.xml',
        'views/snippets/s_quotes_carousel.xml',
    ],
    'images': [
        'static/description/real_estate_description.png',
        'static/description/real_estate_screenshot.jpg',
    ],
    'license': 'LGPL-3',
    'live_test_url': 'https://theme-real-estate.odoo.com',
}
