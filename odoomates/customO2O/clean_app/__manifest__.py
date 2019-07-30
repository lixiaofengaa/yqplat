{
    'name': '保洁服务',
    'version': '12.0.1.0',
    'license': 'LGPL-3',
    'summary': '万国odoo：负责保洁区域划分、人员、清洁记录以及卫生检查管理',
    'depends': ['base'],
    'author': "万国车世界",
    'website': 'http://www.baoshunchem.com/',
    'description': """Clean Management""",
    'category': '万国',
    'data': [
            'security/clean_security.xml',
            'security/ir.model.access.csv',
            'views/clean_menu.xml',
            'views/area_view.xml',
            'views/record_view.xml',
            'views/inspection_view.xml',
            'views/tool_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}