from odoo import api, fields, models


class Charges(models.Model):
    _name = 'parking.charges'
    _description = 'Charges'
    name = fields.Selection(
        [('0', 'A类'),
         ('1', 'B类'),
         ('2', 'C类'),
         ('3', 'D类'),
         ('4', 'E类')]
    )
    space = fields.Char(string='车位位置')
    area = fields.Float(string='车位大小')
    vehicel = fields.Char(string='车辆类型')
    emissions = fields.Float(string='车排放量')
    manage = fields.Float(String='管理费')
    rent = fields.Float(String='租金')
    deposit = fields.Float(String='押金')
    total = fields.Float(String='总计', compute='sum')

    @api.depends('manage', 'rent', 'deposit')
    def sum(self):
        for s in self:
            s.total = s.manage+s.rent+s.deposit
