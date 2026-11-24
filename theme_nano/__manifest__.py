{
    'name': 'Nano Theme',
    'description': 'Discovery block opens onto a parallax scene, text-driven sections, key visuals, an image-text-overlap layout, and a basic team grid before references, KPIs, and a centered call-to-action, kept photo-driven with restrained styling. Story-led and image-forward / suited for creative agencies, makers, design studios, and creative-IT services',
    'category': 'Theme/Lifestyle',
    'summary': 'Maker, Agencies, Creative, Design, IT, Services, Fancy',
    'sequence': 270,
    'version': '2.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/snippets/s_key_images.xml',
        'views/snippets/s_parallax.xml',
        'views/snippets/s_references.xml',
        'views/snippets/s_text_block.xml',
        'views/snippets/s_discovery.xml',
        'views/snippets/s_numbers.xml',
        'views/snippets/s_image_text_overlap.xml',
        'views/snippets/s_company_team_basic.xml',
    ],
    'images': [
        'static/description/nano_cover.gif',
        'static/description/nano_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_discovery', 's_parallax', 's_text_block', 's_key_images', 's_image_text_overlap', 's_company_team_basic', 's_references', 's_numbers', 's_cta_centered'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_key_images'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'dynamic_snippet_args': {
                'content_data': {
                    'alignment': 'left',
                },
                'wrapper_data': {
                    'rounded': 4,
                    'gap': 4,
                },
            },
            'add_classes': [
                'pt88', 'pb112'
            ],
            'remove_classes': [
                'pt64', 'pb64', 's_dynamic_category_no_arrows',
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_nano/static/src/js/tour.js',
        ],
    }
}
