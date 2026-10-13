{
    'name': 'Theme EVMotiv',
    'description': 'Premium hero with cinematic animations opens onto a dynamic carousel showcasing electric vehicle models, innovation-focused feature cards with sustainable design elements, professional team grid, and compelling text-image sections accented by fluid wave motifs. Luxury aesthetic meets cutting-edge technology with sleek transitions, modern typography, and eco-conscious storytelling - designed for premium electric vehicle brands, high-end EV dealerships, luxury mobility solutions, charging network providers, and next-generation sustainable transportation companies seeking sophisticated digital presence',
    'summary': 'Electric Vehicles, EV, E-mobility, Luxury Cars, Sustainable Transport, Green Technology, Premium Automotive, Charging Stations',
    'version': '1.0.0',
    'author': 'Alay Patel (alap)',
    'category': 'Theme/Services',
    'sequence': 140,
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',
        'views/snippets/s_cover.xml',
        'views/snippets/s_carousel.xml',
        'views/snippets/s_cards_grid.xml',
        'views/snippets/s_company_team_grid.xml',
        'views/snippets/s_text_image.xml',
        'views/footer.xml',
    ],
    'images': [
        'static/description/evmotiv_description.png',
        'static/description/evmotiv_screenshot.png',
    ],
    'configurator_snippets': {
        'homepage': ['s_cover', 's_text_image'],
    },
    'assets': {
        'web.assets_frontend': [
            'theme_evmotiv/static/fonts/*',
            'theme_evmotiv/static/src/scss/font.scss',
        ],
        'website.assets_editor': [
            'theme_evmotiv/static/src/js/tour.js',
        ],
    },
    'license': 'LGPL-3',
}
