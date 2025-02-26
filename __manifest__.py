{
    'name': 'Gestion Immobilière',
    'version': '1.0',
    'summary': 'Module pour la gestion immobilière',
    'description': 'Module pour gérer les propriétés, les contrats et les clients',
    'author': 'jasmin',
    'depends': ['base'],
    'data': [
        'security/real_estate_security.xml',
        'security/ir.model.access.csv',
        'views/property_views.xml',
        'views/contract_views.xml',
        'views/client_views.xml',
    ],
    'installable': True,
    'application': True,
}
