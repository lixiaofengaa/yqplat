{
    'name': "商铺商品",
    'summary': "后台管理：商铺商品管理",
    'description': """Long description""",
    'author': "万国车世界",
    'license': "AGPL-3",
    'website': "http://www.baidu.com",
    'depends': ['base'],
    'application': True,
    'installable': True,
    'auto_install': False,
    'data': [
        'security/shop_goods_security.xml',
        'security/ir.model.access.csv',
        # 'views/library_book.xml',
        # 'views/book_view.xml',
        # 'views/book_list_template.xml'
        'views/parent_menu_view.xml',
        'views/shop_view.xml'
        ],
    'category': '万国',
}
