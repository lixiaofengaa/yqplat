{
    'name': '三表管理',
    'version': '12.0.1.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'author': "万国车世界",
    'website': 'http://www.baoshunchem.com/',
    'description': """Surface Management""",
    'installable': True,
    'application': True,
    'auto_install': False,
    'category': '万国',
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
