from odoo import fields, models


class FinancePay(models.Model):

    _name = 'finance.pay.view'
    _description = '支付信息'
    #name = fields.Many2one( 'resource.customer',string='用户',)
    payTitle = fields.Char(string='标题')
    payType = fields.Selection(
        [
            ('0', '通告'),
            ('1', '新闻'),
            ('2', '文章')
        ]
        ,string='类别'
    )
    paySummary = fields.Char(string='概要')
    payUser = fields.Char(string='发布人')
    payTime = fields.Datetime(string='发布时间')
    payWay = fields.Selection(
        [
            ('0', '电脑'),
            ('0', '手机')
        ]
        ,string='发布方式'
    )
    payEndTime = fields.Datetime(string='有效期')
    payIsTop = fields.Selection(
        [
            ('0', '是'),
            ('1', '否'),
        ]
        ,string='是否置顶'
    )
