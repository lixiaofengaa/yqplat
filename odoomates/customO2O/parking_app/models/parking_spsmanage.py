from odoo import api, fields, models


class Spsmanage(models.Model):
    _name = 'parking.spsmanage'
    _description = 'Spsmanage'
    name = fields.Many2one(
        'parking.space',
        string='已售车位'
    )
    cost = fields.Float(string='管理费用(/年)')
    date_start = fields.Date(string='开始时间')
    date_end = fields.Date(string='结束时间')
    year = fields.Integer(string='共几年')
    total = fields.Float(String='总计', compute='sum')

    @api.depends('year', 'cost')
    def sum(self):
        for s in self:
            s.total = s.year * s.cost

