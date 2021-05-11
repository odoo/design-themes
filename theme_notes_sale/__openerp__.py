{
    'name': 'Theme Notes eCommerce Plugin',
    'description': 'Notes eCommerce Plugin',
    'category': 'Hidden',
    'sequence': 281,
    'version': '1.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_notes', 'website_sale'],
    'data': [
        'views/theme.xml',
        'views/layout.xml',
    ],
    'demo': [
        'demo/products.xml',
    ],
    'auto_install': True,
}
