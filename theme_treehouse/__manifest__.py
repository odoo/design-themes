{
    'name': 'Treehouse Theme',
    'description': 'Asymmetric side-grid layout opens with numbered impact stats, color-blocked sections, partner references, and a freegrid showcase, with wavy line motifs accenting the side-grid hero. Image-led with stats and partner proof / suited for environmental NGOs, sustainable development non-profits, ecology initiatives, and conscious travel organizations',
    'category': 'Theme/Environment',
    'summary': 'Environment, Nature, Ecology, Sustainable Development, Non Profit, NGO, Travels',
    'sequence': 140,
    'version': '2.0.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images_library.xml',

        'views/snippets/s_color_blocks_2.xml',
        'views/snippets/s_numbers_list.xml',
        'views/snippets/s_freegrid.xml',
        'views/snippets/s_references.xml',
        'views/snippets/s_sidegrid.xml',
    ],
    'images': [
        'static/description/treehouse_cover.webp',
        'static/description/treehouse_screenshot.webp',
    ],
    'configurator_snippets': {
        'homepage': ['s_sidegrid', 's_numbers_list', 's_color_blocks_2', 's_references', 's_freegrid'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_color_blocks_2'),
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
                    'size': 'small',
                },
            },
            'background': {
                'color': 'o_cc2',
                'shape': {
                    'data-oe-shape-data': '{"shape":"web_editor/Connections/09", "colors":{"c5":"o-color-4"}, "flip":["x"]}',
                    'element': """<div class="o_we_shape o_web_editor_Connections_09" style="background-image: url('/web_editor/shape/web_editor/Connections/09.svg?c5=o-color-4&amp;flip=x');""",
                },
            },
            'add_classes': [
                'pt88', 'pb144',
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
            'theme_treehouse/static/src/js/tour.js',
        ],
    }
}
