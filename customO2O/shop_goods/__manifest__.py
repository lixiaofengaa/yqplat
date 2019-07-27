{
    'name': "商铺商品", # 插件的标题
    'version': '1.0.1',
    'summary': "对商铺、商品、订单的详细管理", # 副标题
    'description': "对商铺、商品、订单的详细管理", # 以RST格式书写的长描述，通常置于三引号中
    'author': "YuQi",
    'sequence':0,
    'license': "AGPL-3", # 证书，常用用AGPL-3，其它选项：LGPL-3或其它OSI证书
    'website': "http://www.baoshunchem.com/", # 获取插件更多详情的网址
    'depends': ['base'], # 所依赖的模块列表，如无，则至少会依赖base
    'category': 'wanguo',
    'application': True,
    'installable': True,
    'data': [
        'security/shop_goods_security.xml',
        'security/ir.model.access.csv',
        # 'views/library_book.xml',
        # 'views/book_view.xml',
        # 'views/book_list_template.xml'
        'views/parent_menu_view.xml',
        'views/shop_view.xml'
        ],
    # 'category': 'Library',
}
