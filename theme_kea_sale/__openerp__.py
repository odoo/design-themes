{
    'name': 'Theme Kea eCommerce Plugin',
    'description': 'Kea eCommerce Plugin',
    'category': 'Hidden',
    'version': '1.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_kea', 'website_sale'],
    'data': [
        'views/theme.xml',
        'views/layout.xml',
    ],
    'demo': [
        'demo/products.xml',
    ],
    'auto_install': True,
}
