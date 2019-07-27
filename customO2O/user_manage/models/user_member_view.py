from odoo import fields, models


class UserMember(models.Model):

    _name = 'user.member.view'
    _description = '会员信息'
    #name = fields.Many2one( 'resource.customer',string='用户',)

    memberTitle = fields.Char(string='账号')
    memberType = fields.Char(string='姓名')
    memberSummary = fields.Char(string='会员等级')
    memberUser = fields.Char(string='会员星级')
    memberTime = fields.Datetime(string='注册时间')
    memberWay = fields.Integer(string='会员折扣')
    memberEndTime = fields.Datetime(string='办理会员时间')
    memberIsTop = fields.Integer(string='会员积分')
