from odoo import api, fields, models


class Own(models.Model):
    _name = 'surface.own'
    _description = 'Own'
    name = fields.Char(
        # 'surface.type',
        # 'own_name',
        string='表的类型'
    )
    num = fields.Integer(string='表号')
    start = fields.Float(string='初始值')
    magn = fields.Float(string='倍率')
    date_stime = fields.Date(string='初始日期')
    range = fields.Float(string='量程')
    house = fields.Integer(string='房间号')


class Record(models.Model):
    _name = 'surface.record'
    _description = 'Record'
    name = fields.Many2one(
        'surface.type',
        string='相关表'
    )
    date_time = fields.Datetime(string='记录的时间')
    numon = fields.Float(string='上次记录表值')
    num = fields.Float(string='本次记录表值')
    cost = fields.Float(string='共计费用')
    balance = fields.Float(string='所欠金额')
    total = fields.Float(string='共计费用', comture='sum')

    @api.depends('cost', 'balance',)
    def sum(self):
        for s in self:
            s.total = s.cost + s.balance
