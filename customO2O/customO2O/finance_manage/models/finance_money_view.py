from odoo import fields, models


class FinanceMoney(models.Model):

    _name = 'finance.money.view'
    _description = '入驻商信息'
    #name = fields.Many2one( 'resource.customer',string='用户',)
    moneyTitle = fields.Char(string='标题')
    moneyType = fields.Selection(
        [
            ('0', '通告'),
            ('1', '新闻'),
            ('2', '文章')
        ]
        ,string='类别'
    )
    moneySummary = fields.Char(string='概要')
    moneyUser = fields.Char(string='发布人')
    moneyTime = fields.Datetime(string='发布时间')
    moneyWay = fields.Selection(
        [
            ('0', '电脑'),
            ('0', '手机')
        ]
        ,string='发布方式'
    )
    moneyEndTime = fields.Datetime(string='有效期')
    moneyIsTop = fields.Selection(
        [
            ('0', '是'),
            ('1', '否'),
        ]
        ,string='是否置顶'
    )
