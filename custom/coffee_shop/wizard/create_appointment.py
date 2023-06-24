from odoo import api, fields, models

class CoffeeBeans(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment wizard"

    name = fields.Char(String= 'Name', required = True)