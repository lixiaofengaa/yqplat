{
    'name': '车位管理',
    'version': '12.0.1.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'author': "万国车世界",
    'website': 'http://www.baoshunchem.com/',
    'description': """Parking Management""",
    'category': '万国',
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'security/parking_security.xml',
        'security/ir.model.access.csv',
        'views/parking_menu.xml',
        'views/space_view.xml',
        'views/charges_view.xml',
        'views/spsmanage_view.xml',
        'views/lease_view.xml',
        'views/temporary_view.xml'
    ],
}