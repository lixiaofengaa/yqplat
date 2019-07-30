from odoo import fields, models


class UserConsumer(models.Model):

    _name = 'user.consumer.view'
    _description = '用户信息'
    #name = fields.Many2one( 'resource.customer',string='用户',)

    consumerTitle = fields.Char(string='姓名')
    consumerType = fields.Selection(
        [
            ('0', '女'),
            ('1', '男')
        ]
        ,string='性别'
    )
    consumerAge = fields.Integer(string='年龄')
    consumerSummary = fields.Char(string='头像')
    consumerUser = fields.Char(string='用户等级')
    consumerTime = fields.Datetime(string='注册时间')
    consumerIsTop = fields.Selection(
        [
            ('0', '是'),
            ('1', '否'),
        ]
        ,string='是否为VIP'
    )
