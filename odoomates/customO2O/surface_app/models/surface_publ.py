from odoo import api, fields, models


class Publ(models.Model):
    _name = 'surface.publ'
    _description = 'Publ'
    name = fields.Char(string='公表编号')
    numstart = fields.Float(string='起始读数')
    range = fields.Float(string='量程')
    chargemode = fields.Char(string='计费方式')
    sharerange = fields.Char(string='分摊范围')
    sharemode = fields.Char(string='分摊方式')
    chargeformula = fields.Char(string='计费公式')


class Copy(models.Model):
    _name = 'surface.copy'
    _description = 'Copy'
    name = fields.Many2one(
        'surface.publ',
        string='公表'
    )
    numup = fields.Float(string='上次表读数')
    num = fields.Float(string='表读数')
    share = fields.Float(string='分摊费用')