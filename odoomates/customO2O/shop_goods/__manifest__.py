{
    'name': "店商", # 插件的标题
    'summary': "店铺、商品、订单管理", # 副标题
    'description': """Long description""", # 以RST格式书写的长描述，通常置于三引号中
    'author': "ZYF", # 作者，多个作者时以逗号间隔
    'license': "AGPL-3", # 证书，常用用AGPL-3，其它选项：LGPL-3或其它OSI证书
    'website': "http://www.baidu.com", # 获取插件更多详情的网址
    'depends': ['base'], # 所依赖的模块列表，如无，则至少会依赖base
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
