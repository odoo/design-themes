{
    'name': 'Theme Anelusia eCommerce Plugin',
    'description': 'Anelusia eCommerce Plugin',
    'category': 'Hidden',
    'version': '1.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_anelusia', 'website_sale'],
    'data': [
        'views/theme.xml',
        'views/layout.xml',
    ],
    'demo': [
        'demo/products.xml',
    ],
    'auto_install': True,
}
