# -*- coding: utf-8 -*-
{
    'name': "统计分析",
    'version': '1.0.1',
    'summary':"对统计管理、智能预警、智能分析进行全方位实施有效率管理",
    'license': 'LGPL-3',
    'category': 'wanguo',
    'sequence':0,
    'depends': ['base'],
    'author': "YuQi",
    'website': 'http://www.baoshunchem.com/',
    'description': "对统计管理、智能预警、智能分析进行全方位实施有效率管理",
    'application': True,
    'installable': True,
    'data': [
        'security/statistics_security.xml',
        'security/ir.model.access.csv',

        'views/statistics_analyse_view.xml',
        'views/statistics_census_view.xml',
        'views/statistics_waring_view.xml',

        'views/statistics_menu.xml',


    ],
    'demo': [
       # 'data/message_demo.xml',
    ],
}
