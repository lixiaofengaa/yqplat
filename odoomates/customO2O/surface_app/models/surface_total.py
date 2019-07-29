from odoo import fields, models


class Total(models.Model):
    _name = 'surface.total'
    _description = 'Total'
    name = fields.Char(string='总表编号')
    numstart = fields.Float()
    chargemode = fields.Char(string='计费方式')
    sharemode = fields.Char(string='分摊方式')
    chargeformula = fields.Char(string='计费公式')
