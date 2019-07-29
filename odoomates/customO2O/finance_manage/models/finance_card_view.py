from odoo import fields, models


class FinanceCard(models.Model):

    _name = 'finance.card.view'
    _description = '会员信息'
    #name = fields.Many2one( 'resource.customer',string='用户',)
    cardTitle = fields.Char(string='标题')
    cardType = fields.Selection(
        [
            ('0', '通告'),
            ('1', '新闻'),
            ('2', '文章')
        ]
        ,string='类别'
    )
    cardSummary = fields.Char(string='概要')
    cardUser = fields.Char(string='发布人')
    cardTime = fields.Datetime(string='发布时间')
    cardWay = fields.Selection(
        [
            ('0', '电脑'),
            ('0', '手机')
        ]
        ,string='发布方式'
    )
    cardEndTime = fields.Datetime(string='有效期')
    cardIsTop = fields.Selection(
        [
            ('0', '是'),
            ('1', '否'),
        ]
        ,string='是否置顶'
    )
