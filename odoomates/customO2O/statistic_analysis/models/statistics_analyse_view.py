from odoo import fields, models


class StatisticsAnalyse(models.Model):

    _name = 'statistics.analyse.view'
    _description = '分析信息'
    #name = fields.Many2one( 'resource.customer',string='用户',)
    analyseTitle = fields.Char(string='分析标题')
    analyseType = fields.Selection(
        [
            ('0', '通告'),
            ('1', '新闻'),
            ('2', '文章')
        ]
        ,string='分析类别'
    )
    analyseSummary = fields.Char(string='分析概要')
    analyseUser = fields.Char(string='发布人')
    analyseTime = fields.Datetime(string='发布时间')
    analyseWay = fields.Selection(
        [
            ('0', '电脑'),
            ('0', '手机')
        ]
        ,string='发布方式'
    )
    analyseEndTime = fields.Datetime(string='有效期')
    analyseIsTop = fields.Selection(
        [
            ('0', '是'),
            ('1', '否'),
        ]
        ,string='是否置顶'
    )
