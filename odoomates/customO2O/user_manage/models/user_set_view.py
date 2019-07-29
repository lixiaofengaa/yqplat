from odoo import fields, models


class UserSet(models.Model):

    _name = 'user.set.view'
    _description = '入驻商信息'
    #name = fields.Many2one( 'resource.customer',string='用户',)
    setTitle = fields.Char(string='姓名')
    setType = fields.Selection(
        [
            ('0', '女'),
            ('1', '男')
        ]
        ,string='性别'
    )
    setAge = fields.Integer(string='年龄')
    setSummary = fields.Char(string='出生年月')
    setUser = fields.Char(string='省份证号')
    setTime = fields.Datetime(string='入驻时间')
    setWay = fields.Char(string='营业执照')
    setEndTime = fields.Datetime(string='合同年限')
    setIsTop = fields.Selection(
        [
            ('0', '是'),
            ('1', '否'),
        ]
        ,string='审核是否通过'
    )
