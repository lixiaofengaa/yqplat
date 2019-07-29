{
    'name': "财务管理平台",
    'version': '12.0.1.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'author': "万国车世界",
    'website': 'http://www.baoshunchem.com/',
    'description': """财务信息管理""",
    'category': '万国',
    'data': [
        'security/finance_security.xml',
        'security/ir.model.access.csv',
        'views/finance_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
