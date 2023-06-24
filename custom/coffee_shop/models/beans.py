from odoo import fields , models, api

class BeansInfo(models.TransientModel):
    _name = "beans.info.transient_model"
    _description = 'Beans Info'
    _rec_name = 'beans_name'

    beans_name = fields.Char(string="Beans_Name", required=True)
    beans_type = fields.Char(string="Type")
    beans_stocks = fields.Integer("stocks")
