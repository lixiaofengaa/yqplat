from odoo import fields, models


class Area(models.Model):
    _name = 'clean.area'
    _description = 'Area'
    name = fields.Selection(
        [('hous3425', '3单元4号楼25楼层'),
         ('hous2509', '2单元5号楼9楼层'),
         ('public04', '小区大门西侧'),
         ('public10','小区北门')],
        string='区域')
    number = fields.Integer(string='区域编号')
    area = fields.Float(string='面积')
    state = fields.Selection(
        [('0', '未清洁'),
         ('1', '已清洁')],
        default='0',
        string='是否清洁'
    )
    cleaner = fields.Many2one(
        'res.partner',
        string='责任人',
    )
    person = fields.Many2one(
        'res.partner',
        string='负责人',
    )
