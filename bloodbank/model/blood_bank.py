# -*- coding: utf-8 -*-

from odoo import models, fields

class BloodBank(models.Model):
    _name = "blood.bank"
    _description = "Blood Bank Management System"

    availability_date = fields.Date('Availability Date',required=True,default=lambda self:fields.Datetime.now())
    name = fields.Char('Name',required=True)
    contact = fields.Char('Contact No.')
    bdate = fields.Date('Birth Date')
    age = fields.Integer('Age')
    doctor_info_id = fields.Many2one('doctor.info', string='Doctor Name')
    employee_info_id = fields.Many2one('employee.info', string='Employee Name')
    email = fields.Char('Email')
    address = fields.Char('Address')
    description = fields.Text('Description',copy=False)
    gender = fields.Selection(
        string='Gender',
        selection=[('male','Male'),('female','Female'),('other','Other')],
    )
    blood_group = fields.Selection(
        string='Blood Group',
        selection=[('ap','A+'),('bp','B+'),('an','A-'),('bn','B-'),('op','O+'),('on','O-'),('abp','AB+'),('abn','AB-')],
    )
    bag_number = fields.Char('Bag Number',copy=False)
    quantity = fields.Integer('Quantity')
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('available', 'Available'),('donated', 'Donated'), ('expired', 'Expired')],
        default='new',
    )

    