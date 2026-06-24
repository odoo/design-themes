{
    'name': 'Orchid Theme',
    'description': 'Sales-led header above a kickoff hero opens onto key visuals, a process-steps narrative, a freegrid showcase, an image-text-overlap layout, and a basic team block before an image wall and references, accented by a varied vocabulary of connection, organic blob, and bold geometric motifs. Process-and-image driven / suited for florists, garden centers, beauty boutiques, and nature-led retail',
    'category': 'Theme/Retail',
    'summary': 'Florist, Gardens, Flowers, Nature, Green, Beauty, Stores',
    'sequence': 230,
    'version': '3.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',

        'views/snippets/s_title.xml',
        'views/snippets/s_images_wall.xml',
        'views/snippets/s_image_text_overlap.xml',
        'views/snippets/s_freegrid.xml',
        'views/snippets/s_company_team_basic.xml',
        'views/snippets/s_process_steps.xml',
        'views/snippets/s_key_images.xml',
        'views/snippets/s_kickoff.xml',
        'views/snippets/s_references.xml',
    ],
    'images': [
        'static/description/orchid_description.webp',
        'static/description/orchid_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_cover_default_image': '/theme_orchid/static/src/img/snippets/s_parallax.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_kickoff', 's_key_images', 's_process_steps', 's_freegrid', 's_image_text_overlap', 's_company_team_basic', 's_title', 's_images_wall', 's_references'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_image_text_overlap'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'dynamic_snippet_args': {
                'content_data': {
                    'alignment': 'left',
                    'size': 'small',
                },
                'wrapper_data': {
                    'gap': 3,
                    'cols_count': 2,
                    'size': 'small',
                },
            },
            'background': {
                'shape': {
                    'data-oe-shape-data': '{"shape":"web_editor/Connections/01", "colors":{"c5":"o-color-3"}, "flip":["x"]}',
                    'element': """<div class="o_we_shape o_web_editor_Connections_01" style="background-image: url('/web_editor/shape/web_editor/Connections/01.svg?c5=o-color-3&amp;flip=x');""",
                },
            },
            'add_classes': [
                'pt104', 'pb152',
                {
                    's_dynamic_snippet_title': 's_dynamic_snippet_title_aside col-lg-3 flex-lg-column justify-content-lg-start'
                },
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
            'theme_orchid/static/src/js/tour.js',
        ],
    }
}
