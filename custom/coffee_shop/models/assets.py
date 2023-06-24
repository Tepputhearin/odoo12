from odoo import fields , models, api

class AssetsInfos(models.AbstractModel):
    _name = "assets.infos.abstract_model"
    _description = 'Assets Info'
    _abstract = True
    _rec_name = 'assets_name'

    assets_name = fields.Char(string="Assets_Name", required=True)
    assets_type = fields.Char(string="stocks")
    assets_stocks = fields.Integer("stocks")

class CustomModel(models.Model):
    _name = 'cus.mdoel.custom_model'
    _description = 'Description of your custom model'
    _inherit = 'assets.infos.abstract_model'