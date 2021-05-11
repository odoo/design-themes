{
    'name': 'Theme Support Engine',
    'category': 'Website',
    'summary': 'Support layer for Themes in 8.0',
    'version': '1.1',
    'description': """
Support layer for themes in 8.0.

This module requires `lessc` and its `clean-css` plugin to be installed on your system. Please refer to the `Less CSS via nodejs` section of https://www.odoo.com/documentation/8.0/setup/install.html#setup-install-source for installation instructions.
        """,
    'author': 'Odoo SA',
    'depends': ['website'],
    'data': [
        'views/snippets.xml',
        'views/themes.xml',
        'views/website_templates.xml',
        'views/website_backend_navbar.xml',
    ],
    'qweb': ['static/src/xml/website.backend.xml'],
    'installable': True,
    'application': False,
}
