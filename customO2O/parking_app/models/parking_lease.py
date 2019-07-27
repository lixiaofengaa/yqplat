from odoo import api, fields, models


class Car(models.Model):
    _name = 'parking.car'
    _description = 'Car'
    name = fields.Char(string='车主姓名')
    nameId = fields.Char(string='车主身份证号')
    carId = fields.Char(string='车牌')
    car = fields.Text(string='车辆基本信息')
    date_end = fields.Datetime(string='缴费截止日期')
    time = fields.Char(string='欠费时长')


class Handle(models.Model):
    _name = 'parking.handle'
    _description = 'Handlle'
    name = fields.Selection(
        [('0', '机动车'),
         ('1', '非机动车')],
        string='车辆类型'
    )
    customer = fields.Char(string='车牌号/客户名')
    space = fields.Many2one(
        'parking.space',
        string='车位信息'
    )
    date_start = fields.Date(string='开始时间')
    date_end = fields.Date(string='结束时间')
    month = fields.Integer(string='共几个月')
    unit = fields.Float(string='费用(/月)')
    cost = fields.Float(string='共计费用',  compute='sum')

    @api.depends('month', 'unit')
    def sum(self):
        for s in self:
            s.cost = s.month * s.unit
