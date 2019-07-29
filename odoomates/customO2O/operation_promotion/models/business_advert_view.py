from odoo import fields, models


class BusinessAdvert(models.Model):

    _name = 'business.advert.view'
    _description = '广告信息'
    #name = fields.Many2one( 'resource.customer',string='用户',)
    advertTitle = fields.Char(string='广告标题')
    advertType = fields.Selection(
        [
            ('0', '饮食'),
            ('1', '娱乐'),
            ('2', '自助')
        ]
        ,string='广告类别'
    )
    advertSummary = fields.Char(string='概要')
    advertUser = fields.Char(string='发布人')
    advertTime = fields.Datetime(string='发布时间')
    advertWay = fields.Selection(
        [
            ('0', '电脑'),
            ('0', '手机')
        ]
        ,string='发布方式'
    )
    advertEndTime = fields.Datetime(string='有效期')
    advertIsTop = fields.Selection(
        [
            ('0', '是'),
            ('1', '否'),
        ]
        ,string='是否下架'
    )
