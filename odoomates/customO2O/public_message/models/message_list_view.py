from odoo import fields, models


class Message(models.Model):

    _name = 'message.list.view'
    _description = '公告信息'
    #name = fields.Many2one( 'resource.customer',string='用户',)
    msgTitle = fields.Char(string='标题')
    msgType = fields.Selection(
        [
            ('0', '通告'),
            ('1', '新闻'),
            ('2', '文章')
        ]
        ,string='类别'
    )
    msgSummary = fields.Char(string='概要')
    msgUser = fields.Char(string='发布人')
    msgTime = fields.Datetime(string='发布时间')
    msgWay = fields.Selection(
        [
            ('0', '电脑'),
            ('0', '手机')
        ]
        ,string='发布方式'
    )
    msgEndTime = fields.Datetime(string='有效期')
    msgIsTop = fields.Selection(
        [
            ('0', '是'),
            ('1', '否'),
        ]
        ,string='是否置顶'
    )
