from odoo import fields, models


class FinanceCash(models.Model):

    _name = 'finance.cash.view'
    _description = '收银台信息'
    #name = fields.Many2one( 'resource.customer',string='用户',)
    cashTitle = fields.Char(string='标题')
    cashType = fields.Selection(
        [
            ('0', '通告'),
            ('1', '新闻'),
            ('2', '文章')
        ]
        ,string='类别'
    )
    cashSummary = fields.Char(string='概要')
    cashUser = fields.Char(string='发布人')
    cashTime = fields.Datetime(string='发布时间')
    cashWay = fields.Selection(
        [
            ('0', '电脑'),
            ('0', '手机')
        ]
        ,string='发布方式'
    )
    cashEndTime = fields.Datetime(string='有效期')
    cashIsTop = fields.Selection(
        [
            ('0', '是'),
            ('1', '否'),
        ]
        ,string='是否置顶'
    )
