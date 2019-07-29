from odoo import fields, models


class BusinessOpera(models.Model):

    _name = 'business.opera.view'
    _description = '用户信息'
    #name = fields.Many2one( 'resource.customer',string='用户',)
    operaTitle = fields.Char(string='店铺账号')
    operaType = fields.Selection(
        [
            ('0', '二维码推广'),
            ('1', '微信推广'),
            ('2', '公众号推广')
        ]
        ,string='推广方式'
    )
    operaSummary = fields.Char(string='推广次数')
    operaUser = fields.Char(string='推广人')
    operaTime = fields.Datetime(string='发布时间')
    operaWay = fields.Selection(
        [
            ('0', '电脑'),
            ('0', '手机')
        ]
        ,string='发布方式'
    )
