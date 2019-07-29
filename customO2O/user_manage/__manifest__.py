# -*- coding: utf-8 -*-
{
    'name': "人员管理",
    'version': '1.0.1',
    'summary':"对入驻商、用户、会员进行全方位实施有效率管理",
    'license': 'LGPL-3',
    'category':'管理类',
    'sequence':0,
    'depends': ['base'],
    'author': "YuQi",
    'website': 'http://www.baoshunchem.com/',
    'description': "对入驻商、用户、会员进行全方位实施有效率管理",
    'application': True,
    'data': [
        'security/user_security.xml',
        'security/ir.model.access.csv',
        'views/user_menu.xml',
        'views/user_set_view.xml',
        'views/user_consumer_view.xml',
        'views/user_member_view.xml',
    ],
    'demo': [
       # 'data/message_demo.xml',
    ],
}
