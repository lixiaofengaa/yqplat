# -*- coding: utf-8 -*-
{
    'name': "运营推广",
    'version': '1.0.1',
    'summary': "对广告、运营、营销活动进行全方位实施有效率管理",
    'license': 'LGPL-3',
    'category': '万国',
    'depends': ['base'],
    'author': "万国车世界",
    'website': 'http://www.baoshunchem.com/',
    'description': "对广告、运营、营销活动进行全方位实施有效率管理",
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'security/business_security.xml',
        'security/ir.model.access.csv',
        'views/business_advert_view.xml',
        'views/business_opera_view.xml',
        'views/business_move_view.xml',
        'views/business_menu.xml',
    ],
    'demo': [
       # 'data/message_demo.xml',
    ],
}
