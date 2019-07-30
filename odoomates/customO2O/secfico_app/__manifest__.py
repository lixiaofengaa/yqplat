{
    'name': '安保消防管理',
    'version': '12.0.1.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'author': "万国车世界",
    'website': 'http://www.baoshunchem.com/',
    'description': """Secfico Management""",
    'category': '万国',
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'security/secfico_security.xml',
        'security/ir.model.access.csv',
        'views/secfico_menu.xml',
        'views/area_view.xml'
    ],
}