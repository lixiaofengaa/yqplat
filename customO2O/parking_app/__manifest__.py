{
    'name': 'Parking Management',
    'version': '12.0.1.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'author': "YuQi",
    'website': 'http://www.baoshunchem.com/',
    'description': """Parking Management""",
    'category': 'wanguo',
    'application': True,
    # 'summary': 'dadsadasdasda',
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