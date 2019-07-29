from odoo import fields, models


class Inspection(models.Model):
    _name = 'clean.inspection'
    _description = 'Inspection'
    name = fields.Many2one(
        'clean.record',
        string='相关保洁记录',
    )
    date_published = fields.Datetime(string='完成时间')
    state = fields.Selection(
        [('0', '很好'),
         ('1', '一般'),
         ('2', '差')],
        default='1',
        string='完成情况'
    )
