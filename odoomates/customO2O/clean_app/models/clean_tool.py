from odoo import fields, models


class Tool(models.Model):
    _name = 'clean.tool'
    _description = 'Tool'
    name = fields.Char(string='工具名称')
    loss = fields.Selection(
        [('0', '崭新'),
         ('1', '完好'),
         ('2', '破旧')],
        string='工具损耗程度'
    )
    employee = fields.Many2one(
        'res.partner',
        string='领用人'
    )
    state = fields.Selection(
        [('0', '已归还'),
         ('1', '未归还')],
        default='1',
        string='工具损耗程度'
    )
