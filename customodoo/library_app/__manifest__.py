{
    'name': 'Library Management',
    'description': 'Manage library book catalogue and lending',
    'author': 'cry',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'data/res.partner.csv',
        'data/library.book.csv',
        'data/book_demo.xml',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/book_list_template.xml'
    ]
}
