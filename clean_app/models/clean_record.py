from odoo import fields, models


class Record(models.Model):
    _name = 'clean.record'
    _description = 'Record'
    name = fields.Integer(string='记录编号')
    project = fields.Selection(
        [('0', '卫生保洁'),
         ('1', '消毒杀菌')],
        string='保洁项目')
    cleaner = fields.Many2one(
        'res.partner',
        string='保洁人员',
    )
    date_published = fields.Datetime(string='保洁时间')
    space = fields.Selection(
        [('hous3425', '3单元4号楼25楼层'),
         ('hous2509', '2单元5号楼9楼层'),
         ('public04', '小区大门西侧'),
         ('public10', '小区北门')],
    )
    state = fields.Selection(
        [('0', '未完成'),
         ('1', '已完成')],
        default='0',
        string='是否完成'
    )
    rema = fields.Text(string='备注')


