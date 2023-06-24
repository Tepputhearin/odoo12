from odoo import fields, models, api

class EmployeeRecords(models.Model):
    _name = "employee.records"
    _description = 'Employee Record'
    _rec_name = 'emp_name'

    emp_name = fields.Char(string="Employee_Name", required=True)
    emp_email = fields.Char(string="Email")
    emp_phone = fields.Integer("Phone")
    image = fields.Binary(string="Image")
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                           index=True, default=lambda self: ('New'))
    @api.model
    def create(self, vals):
        if vals.get('name_seq', ('New')) == ('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('employee.records.sequence') or ('New')
        result = super(EmployeeRecords, self).create(vals)
        return result