# -*- coding: utf-8 -*-
{
    'name': "人员管理",
    'version': '1.0.1',
    'summary': "后台管理：对入驻商、用户、会员进行全方位实施有效率管理",
    'license': 'LGPL-3',
    'category': '万国',
    'depends': ['base'],
    'author': "万国车世界",
    'website': 'http://www.baoshunchem.com/',
    'description': "对入驻商、用户、会员进行全方位实施有效率管理",
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'security/ir.model.access.csv',
        'security/user_security.xml',
        'views/user_menu.xml',
        'views/user_set_view.xml',
        'views/user_consumer_view.xml',
        'views/user_member_view.xml',
    ],
    'demo': [
       # 'data/message_demo.xml',
    ],
}
