from odoo import fields, models, api


class DecorateRegister(models.Model):
    _name = 'property.decorate.register'
    _description = '装修信息登记'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='申请编号')
    applicant = fields.Char(string='装修申请人', required=True)
    phone = fields.Char(string='联系电话', required=True)
    description = fields.Text(string='装修内容描述')
    date_start = fields.Date(string='期望起始日期', required=True)
    date_end = fields.Date(string='期望结束日期', required=True)
    house = fields.One2many(
        'property.estate',
        'register_id',
        string='房间信息'
    )
    state = fields.Selection(
        [('open', '已登记'),
         ('handle', '已受理'),
         ('done', '已完成')],
        string='装修进度',
    )
    register_id = fields.Many2one('property.decorate.handle')


class DecorateHandle(models.Model):
    _name = 'property.decorate.handle'
    _description = '装修申请信息获取并上门处理'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Many2one('res.partner', string='维修员工姓名')
    phone = fields.Char(string='联系电话')
    register_ids = fields.One2many(
        'property.decorate.register',
        'register_id',
        string='装修申请信息'
    )
    material_ids = fields.One2many(
        'property.material',
        'material_id',
        string='装修领料'
    )
    state = fields.Selection(
        [('open', '已受理'),
         ('done', '已完工')],
        string='维修进度'
    )


class DecorateCheck(models.Model):
    _name = 'property.decorate.check'
    _description = '装修验收以及意见反馈和员工评价'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Selection(string='申请编号', selection='_get_number')
    applicant = fields.Char(string='装修申请人', required=True)
    information = fields.Text(string='装修申请内容')
    decorator = fields.Many2one('res.partner', string='装修员工', required=True)
    evaluate = fields.Selection(
        [('one', '满意'),
         ('two', '一般'),
         ('three', '不满意')],
        string='维修员供评价'
    )
    state = fields.Selection(
        [('wait', '待确认'),
         ('close', '已确认验收')],
        string='验收审核'
    )
    suggesstion = fields.Text(string='意见反馈')

    @api.model
    def _get_number(self):
        registers = self.env['property.decorate.register'].search([])
        return [(register.name, register.name) for register in registers]

    @api.onchange('name')
    def _get_description(self):
        register = self.env['property.decorate.register'].search([('name', '=like', self.name)])
        self.information = register.description
        self.applicant = register.applicant


class DecoratePay(models.Model):
    _name = 'property.decorate.pay'
    _description = '装修缴费管理'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Selection(string='申请编号', selection='_get_number')
    applicant = fields.Char(string='装修申请人', required=True)
    money = fields.Float(string='支付金额', required=True)
    pay_way = fields.Selection(
        [('cash', '现金'),
         ('ali', '支付宝'),
         ('wechat', '微信'),
         ('card', '刷卡')],
        string='支付方式'
    )
    @api.model
    def _get_number(self):
        registers = self.env['property.decorate.register'].search([])
        return [(register.name, register.name) for register in registers]

    @api.onchange('name')
    def _get_description(self):
        register = self.env['property.decorate.register'].search([('name', '=like', self.name)])
        self.information = register.description
        self.applicant = register.applicant