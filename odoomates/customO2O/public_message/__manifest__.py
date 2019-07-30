# -*- coding: utf-8 -*-
{
    'name': "公告信息",
    'version': '1.0.1',
    'summary':"对全体用户公告通知或新闻、文章推送",
    'license': 'LGPL-3',
    'category': '万国',
    'sequence':0,
    'depends': ['base'],
    'author': "万国车世界",
    'website': 'http://www.baoshunchem.com/',
    'description': "对全体用户公告通知或新闻、文章推送",
    'installable': True,
    'application': True,
    'auto_install': False,
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
