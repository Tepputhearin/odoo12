from odoo import api, models

class BeansReportXLSX(models.AbstractModel):
    _name = 'report.coffee_shop.report_template'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['employee.records'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'employee.records',
            'docs': docs,
        }