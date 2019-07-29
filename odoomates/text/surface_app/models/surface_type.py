from odoo import fields, models


class Type(models.Model):
    _name = 'surface.type'
    _description = 'Type'
    name = fields.Selection(
        [('0', '水表'),
         ('1', '电表'),
         ('2', '煤气表')],
        string='仪表类型'
    )
    unit = fields.Float(string='计费标准(元/升/度/方)')
    remarks = fields.Text(string='备注')
    # own_name = fields.Many2one('surface.own')
