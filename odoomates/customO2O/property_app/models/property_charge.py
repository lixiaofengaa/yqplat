from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Charge(models.Model):
    _name = 'property.charge'
    _description = '收费管理'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    type = fields.Selection(
        [('period', '周期性收费'),
         ('instrument', '抄表类收费'),
         ('transient', '临时性收费')],
        string='项目类别'
    )
    name = fields.Char(
        string='名称',
        required=True
    )
    compute = fields.Char(
        default='单价*数量',
        string='金额计算方式',
        readonly=True
    )
    price = fields.Float(string='单价', help='单位：元')
    style = fields.Selection(
        [('area', '建筑面积'),
         ('area_inter', '套内面积')],
        string='计量方式'
    )
    charge_id = fields.Many2one('property.contract')


class ChargePay(models.Model):
    _name = 'property.charge.pay'
    _description = '客户缴费'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='合同编号', required=True)
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
    customer = fields.Char(
        string='用户名称',
        compute='_get_name'
    )

    @api.depends('house', 'building', 'home')
    def _get_name(self):
        for s in self:
            estate = s.env['property.estate'].search(
                [('house', '=', s.house), ('building', '=', s.building), ('home', '=', s.home)])
            s.customer = estate.name

    charge_description = fields.Selection(
        [('home', '房租'),
         ('water', '水费'),
         ('electric', '电费'),
         ('garbage', '垃圾费')],
        string='收费描述')
    date_start = fields.Datetime(string='起始日期')
    date_end = fields.Datetime(string='结束日期')
    money = fields.Float(string='支付金额', default=0)
    money_discount = fields.Float(string='优惠金额', d1efault=0)
    overdue_fine = fields.Float(string='滞纳金', default=0)
    money_count = fields.Float(string='总计', compute='_onchange_compute_money_count')
    state = fields.Selection(
        [('new', '未出单'),
         ('done', '已出单')],
        string='账单状态')

    @api.depends('money', 'money_discount', 'overdue_fine')
    def _onchange_compute_money_count(self):
        for s in self:
            if s.money < 0.0 or s.money_discount < 0.0 or s.overdue_fine < 0.0:
                raise ValidationError('输入的金额不能小于0')
            if s.money + s.overdue_fine < s.money_discount:
                s.money_count = 0.0
            s.money_count = s.money - s.money_discount + s.overdue_fine


class Payment(models.Model):
    _name = 'property.charge.payment'
    _description = '用户缴费管理'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Selection(string='合同编号', selection='_get_number')

    @api.model
    def _get_number(self):
        bills = self.env['property.charge.pay'].search([])
        return [(bill.name, bill.name) for bill in bills]

    customer = fields.Char(string='用户名称', compute='_get_customer')
    count = fields.Float(string='待支付金额', compute='_get_customer', readonly=True)
    @api.multi
    @api.onchange('name')
    def _get_customer(self):
        for s in self:
            bill = s.env['property.charge.pay'].search([('name', '=like', s.name)])
            s.customer = bill.customer
            s.count = bill.money_count

    money_other = fields.Float(string='其他待支付金额')
    count_pay = fields.Float(string='总计', compute='_compute_count')
    @api.multi
    @api.depends('count', 'money_other')
    def _compute_count(self):
        for s in self:
            if s.money_other < 0:
                raise ValidationError('输入的金额必须大于零')
            s.count_pay = sum([s.count, s.money_other])
    pay_type = fields.Selection(
        [('money', '现金'),
         ('ali', '支付宝'),
         ('wechat', '微信'),
         ('card', '银行卡')],
        string='支付方式'
    )
    state = fields.Selection(
        [('new', '未支付'),
         ('done', '已支付')],
        string='支付状态')


class ChargePre(models.Model):
    _name = 'property.charge.pre'
    _description = '用户日常费用预交管理'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Selection(string='用户名称', selection='_get_customer')


class ChargeDetail(models.Model):
    _name = 'property.charge.detail'
    _description = '用户日常费用详情管理'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Selection(string='用户名称', selection='_get_customer')

    def _get_customer(self):
        customers = self.env['property.customer'].searcr([])
        return [(customer.customer_id, customer.name) for customer in customers]
    money_water = fields.Float(string='水费明细')
    money_electric = fields.Float(string='电费明细')
    money_gas = fields.Float(string='燃气费明细')
    money_count = fields.Float(string='生活费用总计', readonly=True)


class ChargeDebt(models.Model):
    _name = 'property.charge.debt'
    _description = '用户欠费管理'


class ChargeQuit(models.Model):
    _name = 'property.charge.quit'
    _description = '用户退款管理'


