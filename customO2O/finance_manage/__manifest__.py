# -*- coding: utf-8 -*-
{
    'name': "财务管理",
    'version': '1.0.1',
    'summary':"对入收银、财务、充值、支付进行全方位实施有效率管理",
    'license': 'LGPL-3',
    'category':'管理类',
    'sequence':0,
    'depends': ['base'],
    'author': "YuQi",
    'website': 'http://www.baoshunchem.com/',
    'description': "对入收银、财务、充值、支付进行全方位实施有效率管理",
    'application': True,
    'data': [
        'security/finance_security.xml',
        'security/ir.model.access.csv',

        'views/finance_cash_view.xml',
        'views/finance_money_view.xml',
        'views/finance_card_view.xml',
        'views/finance_pay_view.xml',

        'views/finance_menu.xml',


    ],
    'demo': [
       # 'data/message_demo.xml',
    ],
}
