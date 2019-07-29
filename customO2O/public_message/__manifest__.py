# -*- coding: utf-8 -*-
{
    'name': "公告信息",
    'version': '1.0.1',
    'summary':"对全体用户公告通知或新闻、文章推送",
    'license': 'LGPL-3',
    'category':'管理类',
    'sequence':0,
    'depends': ['base'],
    'author': "YuQi",
    'website': 'http://www.baoshunchem.com/',
    'description': "对全体用户公告通知或新闻、文章推送",
    'application': True,
    'data': [
        'security/message_security.xml',
        'security/ir.model.access.csv',
        'views/message_menu.xml',
        'views/message_list_view.xml',
    ],
    'demo': [
       # 'data/message_demo.xml',
    ],
}
