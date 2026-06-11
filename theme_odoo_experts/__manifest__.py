{
    'name': 'Experts Theme',
    'description': 'Mockup hero leads into client references, alternating image-and-text proof rows, a feature showcase, and a collapsible FAQ before a CTA with device-mockup framing (phone, browser, tablet, laptop) running across the proof rows and underline highlights on key headings, accented by connection line motifs at the closing block. Credentials-and-proof driven / suited for business advisors, corporate consultancies, finance services, and IT advisory firms',
    'category': 'Theme/Corporate',
    'summary': 'Advisor, Corporate, Service, Business, Finance, IT',
    'sequence': 210,
    'version': '2.1.0',
    'depends': ['website'],
    'data': [
        'data/generate_primary_template.xml',
        'data/ir_asset.xml',
        'views/images.xml',

        'views/snippets/s_cta_box.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_references.xml',
        'views/snippets/s_references_lite.xml',
        'views/snippets/s_showcase.xml',
        'views/snippets/s_mockup_image.xml',
    ],
    'images': [
        'static/description/odoo_experts_description.webp',
        'static/description/odoo_experts_screenshot.webp',
    ],
    'images_preview_theme': {
        'website.s_image_text_device': '/theme_odoo_experts/static/src/img/snippets/s_image_text_device.webp',
        'website.s_text_image_default_image': '/theme_odoo_experts/static/src/img/snippets/s_text_image.webp',
        'website.s_image_text_default_image': '/theme_odoo_experts/static/src/img/snippets/s_image_text.webp',
        'website.s_showcase_default_image': '/theme_odoo_experts/static/src/img/snippets/s_showcase_default_image.webp',
        'website.library_image_08': '/theme_odoo_experts/static/src/img/snippets/library_image_08.webp',
        'website.s_picture_default_image': '/theme_odoo_experts/static/src/img/snippets/s_picture.webp',
    },
    'configurator_snippets': {
        'homepage': ['s_mockup_image', 's_references_lite', 's_image_text', 's_text_image', 's_showcase', 's_faq_collapse', 's_cta_box'],
    },
    'configurator_snippets_addons': {
        'website_sale': {
            'homepage': [
                ('website_sale.s_dynamic_snippet_category_list', 'after', 's_showcase'),
            ],
        },
    },
    'theme_customizations': {
        'website_sale.s_dynamic_snippet_category_list': {
            'template_key': (
                'website_sale.dynamic_filter_template_product_public_category_default'
            ),
            'data_attributes': {
                'rounded': '4',
                'gap': '4',
                'button': 'Explore Now'
            },
            'add_classes': [
                'pt40',
            ],
            'remove_classes': [
                's_dynamic_category_clickable_items', 'pt64',
            ],
        },
    },
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
    'assets': {
        'website.assets_editor': [
            'theme_odoo_experts/static/src/js/tour.js',
        ],
    }
}
