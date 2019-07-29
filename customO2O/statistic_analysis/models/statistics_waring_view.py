from odoo import fields, models


class StatisticsWaring(models.Model):

    _name = 'statistics.waring.view'
    _description = '警告信息'
    #name = fields.Many2one( 'resource.customer',string='用户',)
    waringTitle = fields.Char(string='标题')
    waringType = fields.Selection(
        [
            ('0', '通告'),
            ('1', '新闻'),
            ('2', '文章')
        ]
        ,string='类别'
    )
    waringSummary = fields.Char(string='概要')
    waringUser = fields.Char(string='发布人')
    waringTime = fields.Datetime(string='警告时间')
    waringWay = fields.Selection(
        [
            ('0', '电脑'),
            ('0', '手机')
        ]
        ,string='警告方式'
    )
    waringEndTime = fields.Datetime(string='有效期')
    waringIsTop = fields.Selection(
        [
            ('0', '是'),
            ('1', '否'),
        ]
        ,string='是否置顶'
    )
