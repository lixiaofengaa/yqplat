from odoo import api, fields, models


class Temporary(models.Model):
    _name = 'parking.temporary'
    _description = 'Temporary'
    name = fields.Char(string='收费地址')
    customer = fields.Char(string='车牌号/客户名')
    category = fields.Selection(
        [('0', '临时停车')],
        string='收费项目'
    )
    date_start = fields.Date(string='开始时间')
    date_end = fields.Date(string='结束时间')
    unit = fields.Float(string='收费标准(/时)')
    hour = fields.Integer(string='共几小时')
    total = fields.Float(String='总计', compute='sum')

    @api.depends('unit', 'hour')
    def sum(self):
        for s in self:
            s.total = s.unit * s.hour