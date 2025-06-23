{
    'name': 'Estate',
    'version': '0.1',
    'summary': 'Real estate management',
    'description': 'Module to manage real estate properties',
    'category': 'Sales',
    'author': 'Your Name',
    'depends': ['base'],
    'installable': True,
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
    ],
    'installable' : True,
    'application' : True,
}
