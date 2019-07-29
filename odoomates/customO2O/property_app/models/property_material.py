from odoo import fields, models


class Material(models.Model):
    _name = 'property.material'
    _description = '物料基础信息'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    customer_id = fields.Char(string='材料编号', required=True)
    name = fields.Char(string='材料名称', required=True)
    brand = fields.Char(string='品牌', required=True)
    type = fields.Char(string='规格型号', required=True)
    uint = fields.Char(string='单位')
    price = fields.Float(string='单价', default=0, required=True)
    count = fields.Integer(string='数量', default=0, required=True)
    import_id = fields.Many2one('property.material.import')
    material_id = fields.Many2one('property.decorate.handle')
    maintain_id = fields.Many2one('property.maintain.handle')


class Supply(models.Model):
    _name = 'property.material.supply'
    _description = '供应商信息'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='供应商名称', required=True)
    address = fields.Char(string='地址', required=True)
    supplier = fields.Char(string='联系人', required=True)
    phone = fields.Char(string='联系电话', required=True)
    mail = fields.Char(string='邮箱')


class Import(models.Model):
    _name = 'property.material.import'
    _description = '物料入库信息'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='入库单号', required=True)
    date_import = fields.Datetime(string='入库日期', required=True)
    supplier = fields.Many2one(
        'property.material.supply',
        string='供应商',
        default=True
    )
    materials = fields.One2many(
        'property.material',
        'import_id',
        string='入库材料详情'
    )


class Export(models.Model):
    _name = 'property.material.export'
    _description = '商品出库信息管理'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='出库单号', required=True)
    date_export = fields.Datetime(string='出库日期', required=True)
    department = fields.Many2one(
        'hr.department',
        string='领料部门',
        default=True
    )
    materials = fields.One2many(
        'property.material',
        'import_id',
        string='出库材料详情'
    )
