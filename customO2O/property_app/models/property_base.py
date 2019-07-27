from odoo import fields, models


class Customer(models.Model):
    _name = 'property.customer'
    _description = '客户信息管理'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    customer_id = fields.Integer(string='客户编号', required=True)
    name = fields.Char(string='客户姓名', required=True)
    phone = fields.Char(string='联系电话', required=True)
    family = fields.One2many(
        'res.partner',
        'partner_id',
        string='家庭成员')
    check_in = fields.One2many(
        'res.partner',
        'partner_id',
        string='入住成员')
    estate = fields.Char(string='房间信息')
    carport = fields.Char(string='车位信息')


class Estate(models.Model):
    _name = 'property.estate'
    _description = '房产管理信息'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='业主姓名', required=True)
    house = fields.Selection(
        [('select1', '金山名都'),
         ('select2', '桂碧园'),
         ('select3', '万象城'),
         ('select4', '上海明珠')],
        string='楼盘',
        required=True
    )
    building = fields.Selection(
        [('one', '1幢'),
         ('two', '2幢'),
         ('three', '3幢'),
         ('four', '4幢')],
        string='楼宇',
        required=True
    )
    home = fields.Selection(
        [('1101', '1-101'),
         ('1102', '1-102'),
         ('1103', '1-103'),
         ('2101', '2-101'),
         ('2102', '2-102'),
         ('2103', '2-103')],
        string='房间号',
        required=True)
    area = fields.Float(string='建筑面积', required=True)
    area_inter = fields.Float(string='套内面积', required=True)
    area_equal = fields.Float(string='公摊面积', required=True)
    state = fields.Selection(
        [('open', '空闲'),
         ('sell', '已售'),
         ('rent', '已租'),
         ('close', '禁用')],
        string='房间状态'
    )
    estate_id = fields.Many2one('property.contract')
    register_id = fields.Many2one('property.decorate.register')


class InstrumentCategory(models.Model):
    _name = 'property.instrument.category'
    _description = '仪表种类管理'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Selection(
        [('electricity', '电表'),
         ('water', '水表'),
         ('gas', '燃气表')],
        string='仪表类型',
        required=True
    )
    unit = fields.Selection(
        [('degree', '度'),
         ('ton', '吨'),
         ('square', '方')],
        string='计量单位',
        required=True
    )


class Department(models.Model):
    _inherit = 'hr.department'


class Employee(models.Model):
    _inherit = 'hr.employee'


class Partner(models.Model):
    _inherit = 'res.partner'
    partner_id = fields.Many2one('property.customer')


