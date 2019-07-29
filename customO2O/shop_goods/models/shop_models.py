from odoo import api, fields, models
from odoo.exceptions import Warning


class Shop(models.Model):
    _name = 'shop.view'
    _description = 'Shop'
    name = fields.Char('商铺名称', required=True)
    category = fields.Selection(
        [('cy', '餐饮'),
         ('yl', '娱乐'),
         ('qx', '汽修')],
        default='cy',
        string='商铺类别'
    )
    local = fields.Char('位置')
    dmxx = fields.Char('店面形象')
    business = fields.Char('主要业务')
    score = fields.Integer(string='商铺评分')
    grade = fields.Integer(string='商铺等级')
    credibility = fields.Integer(string='信誉度')
    judge = fields.Selection(
        [('ff', '否'),
         ('yy', '是')],
        default='ff',
        string='是否有实体商铺'
    )
    type = fields.Selection(
        [('zy', '自营'),
         ('st', '实体'),
         ('xn', '虚拟')],
        default='zy',
        string='商铺类型'
    )
