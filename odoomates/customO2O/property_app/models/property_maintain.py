from odoo import fields, models, api


class Maintain(models.Model):
    _name = 'property.maintain'
    _description = '维修信息管理'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='维修编号', required=True)
    applicant = fields.Char(string='业主姓名')
    phone = fields.Char(string='联系电话')
    house = fields.Selection(
        [('select1', '金山名都'),
         ('select2', '桂碧园'),
         ('select3', '万象城'),
         ('select4', '上海明珠')],
        string='楼盘',
        required=True
    )
    building = fields.Selection(
        [('one', '1幢'),
         ('two', '2幢'),
         ('three', '3幢'),
         ('four', '4幢')],
        string='楼宇',
        required=True
    )
    home = fields.Char(string='房间号', required=True)
    description = fields.Text(string='故障描述')
    state = fields.Selection(
        [('open', '已报修'),
         ('handle', '已受理'),
         ('done', '已完成')],
        string='维修进度',
    )
    maintain_id = fields.Many2one('property.maintain.handle')


class DecorateHandle(models.Model):
    _name = 'property.maintain.handle'
    _description = '保修申请信息获取并处理'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Many2one('res.partner', string='维修员工姓名')
    phone = fields.Char(string='联系电话')
    register_ids = fields.One2many(
        'property.maintain',
        'maintain_id',
        string='维修申请信息'
    )
    material_ids = fields.One2many(
        'property.material',
        'maintain_id',
        string='维修领料'
    )
    state = fields.Selection(
        [('open', '已受理'),
         ('done', '已完工')],
        string='维修进度'
    )


class DecorateCheck(models.Model):
    _name = 'property.maintain.check'
    _description = '维修验收以及意见反馈和员工评价'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Selection(string='报修编号', selection='_get_number')
    applicant = fields.Char(string='报修申请人', required=True)
    information = fields.Text(string='报修申请内容')
    decorator = fields.Many2one('res.partner', string='维修员工', required=True)
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
        maintains = self.env['property.maintain'].search([])
        return [(maintain.name, maintain.name) for maintain in maintains]

    @api.onchange('name')
    def _get_description(self):
        register = self.env['property.maintain'].search([('name', '=like', self.name)])
        self.information = register.description
        self.applicant = register.applicant


class DecoratePay(models.Model):
    _name = 'property.maintain.pay'
    _description = '维修缴费管理'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Selection(string='报修编号', selection='_get_number')
    applicant = fields.Char(string='报修申请人', required=True)
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
        registers = self.env['property.maintain'].search([])
        return [(register.name, register.name) for register in registers]

    @api.onchange('name')
    def _get_description(self):
        register = self.env['property.maintain'].search([('name', '=like', self.name)])
        self.applicant = register.applicant
