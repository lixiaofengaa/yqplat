{
    'name': '绿化管理',
    'version': '12.0.1.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'summary': '万国odoo：负责园区绿化区域、植被以及绿化计划和检查管理',
    'author': "万国车世界",
    'website': 'http://www.baoshunchem.com/',
    'description': """Green Management""",
    'category': '万国',
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'security/green_security.xml',
        'security/ir.model.access.csv',
        'views/green_menu.xml',
        'views/botany_view.xml'
    ],
}