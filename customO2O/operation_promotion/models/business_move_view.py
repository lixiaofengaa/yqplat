from odoo import fields, models


class BusinessMove(models.Model):

    _name = 'business.move.view'
    _description = '推广活动信息'
    #name = fields.Many2one( 'resource.customer',string='用户',)
    moveTitle = fields.Char(string='活动主题')
    moveType = fields.Selection(
        [
            ('0', '打折'),
            ('1', '优惠卷'),
            ('2', '奖品'),
            ('3', '积分')
        ]
        ,string='活动类别'
    )
    moveSummary = fields.Char(string='活动概要')
    moveUser = fields.Char(string='发布人')
    moveTime = fields.Datetime(string='发布时间')
    moveWay = fields.Selection(
        [
            ('0', '电脑'),
            ('0', '手机')
        ]
        ,string='发布方式'
    )
    moveEndTime = fields.Datetime(string='有效期')
    moveIsTop = fields.Selection(
        [
            ('0', '是'),
            ('1', '否'),
        ]
        ,string='是否置顶'
    )
    moveAim = fields.Char(string='活动目的')