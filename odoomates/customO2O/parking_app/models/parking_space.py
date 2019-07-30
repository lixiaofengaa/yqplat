from odoo import fields, models


class Space(models.Model):
    _name = 'parking.space'
    _description = 'Space'
    name = fields.Integer(string='车位编号')
    category = fields.Selection(
        [('0', '售卖'),
         ('1', '长租'),
         ('2', '临停'),
         ('3', '待租')],
        string='车位状态'
    )
    space = fields.Char(string='车位地址')
