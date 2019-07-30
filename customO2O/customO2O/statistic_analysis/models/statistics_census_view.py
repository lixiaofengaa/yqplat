from odoo import fields, models


class StatisticsCensus(models.Model):

    _name = 'statistics.census.view'
    _description = '预警信息'
    #name = fields.Many2one( 'resource.customer',string='用户',)
    censusTitle = fields.Char(string='预警标题')
    censusType = fields.Selection(
        [
            ('0', '通告'),
            ('1', '新闻'),
            ('2', '文章')
        ]
        ,string='类别'
    )
    censusSummary = fields.Char(string='预警概要')
    censusUser = fields.Char(string='发布人')
    censusTime = fields.Datetime(string='发布时间')
    censusWay = fields.Selection(
        [
            ('0', '电脑'),
            ('0', '手机')
        ]
        ,string='发布方式'
    )
    censusEndTime = fields.Datetime(string='有效期')
    censusIsTop = fields.Selection(
        [
            ('0', '是'),
            ('1', '否'),
        ]
        ,string='是否置顶'
    )
