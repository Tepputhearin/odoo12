{
    'name' : 'Coffee Management',
    'version' : '12.0',
    'summary': 'Module for managing coffee shops',
    'sequence': '10',
    'description':"" ,
    'category': 'Extra Tools',
    'website': 'https://www.odoo.com',
    'depends' : [
        'report_xlsx_nexus'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'wizard/create_appointment_view.xml',
        'views/employee_view.xml',
        'views/bean_view.xml',
        'reports/report.xml',
        'reports/beans_report.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}