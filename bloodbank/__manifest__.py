# -*- coding: utf-8 -*-
{
    'name' : 'Blood Bank Management System',
    'description' : """"this is Blood Bank Management System""",
    'depends': ['mail'],
    'data' : [
        'security/ir.model.access.csv',
        'views/blood_bank_menu.xml',
        'views/blood_bank_view.xml',
        'views/doctor_info_view.xml',
        'views/employee_info_view.xml',
        'views/blood_group_view.xml',
    ],
    'demo': [
        'demo/blood_bank_doc_demo.xml',
        'demo/blood_bank_employee_demo.xml',
        'demo/blood_bank_demo_data.xml',
        'demo/blood_group_demo.xml',
    ],
    'application' : True,
}