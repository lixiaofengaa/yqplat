from odoo import fields, models, api


class Contract(models.Model):
    _name = 'property.contract'
    _description = '租赁合同管理'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    contract_id = fields.Char(string='合同编号', required=True)
    name = fields.Char(string='合同名称', required=True)
    customer = fields.Many2one(
        'property.customer',
        string='客户',
        required=True)
    date_start = fields.Datetime(string='起始日期', required=True)
    date_end = fields.Datetime(string='结束日期', required=True)

    @api.constrains('date_end')
    def _check_date_end(self):
        if self.date_end < self.date_start:
            raise ValueError('结束日期必须大于起始日期')

    state = fields.Selection(
        [('open', '空闲'),
         ('trophy', '自营'),
         ('lease', '出租')],
        string='房屋状态',
        required=True
    )
    home = fields.One2many(
        'property.estate',
        'estate_id',
        string='房间明细'
    )
    cost = fields.One2many(
        'property.charge',
        'charge_id',
        string='收费明细'
    )


class ContractRent(models.Model):
    _name = 'property.contract.rent'
    _description = '租金管理'





