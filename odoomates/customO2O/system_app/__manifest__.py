{
    'name': "系统设置",
    'version': '12.0.1.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'author': "万国车世界",
    'website': 'http://www.baoshunchem.com/',
    'description': """系统设置""",
    'category': '万国',
    'data': [
        'security/system_security.xml',
        'security/ir.model.access.csv',
        'views/system_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
