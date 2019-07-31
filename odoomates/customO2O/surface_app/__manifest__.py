{
    'name': '三表管理',
    'version': '12.0.1.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'author': "YuQi",
    'website': 'http://www.baoshunchem.com/',
    'description': """三表管理""",
    'application': True,
    # 'summary': '',
    'data': [
        'security/surface_security.xml',
        'security/ir.model.access.csv',
        'views/surface_menu.xml',
        'views/type_view.xml',
        'views/own_view.xml',
        'views/publ_view.xml',
        'views/total_view.xml'
    ],
}
