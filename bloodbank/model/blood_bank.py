# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import datetime, time

class BloodBank(models.Model):
    _name = "blood.bank"
    _description = "Blood Bank Management System"
    _inherit = ['mail.thread','mail.activity.mixin'] #to add the chatter 

    availability_date = fields.Date('Availability Date',required=True,default=lambda self:fields.Datetime.now())
    name = fields.Char('Name',required=True)
    contact = fields.Char('Contact No.')
    date_of_birth = fields.Date('Birth Date')
    age = fields.Integer('Age')
    doctor_info_id = fields.Many2one('doctor.info', string='Doctor Name', tracking=True)
    employee_info_id = fields.Many2one('employee.info', string='Employee Name', tracking=True)
    blood_group_id = fields.Many2one('blood.group', string='Blood Group', tracking=True)
    issue_ids = fields.Many2many("medical.issue", string="Medical Issues")
    email = fields.Char('Email')
    address = fields.Char('Address')
    gender = fields.Selection(
        string='Gender',
        selection=[('male','Male'),('female','Female'),('other','Other')],
    )
    
    bag_number = fields.Char('Bag Number',copy=False)
    quantity = fields.Integer('Quantity', tracking=True)
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('available', 'Available'),('donated', 'Donated'), ('expired', 'Expired')],
        default='new',
        tracking=True,
    )

    def blood_donated(self):
        for record in self:    
                record.state = 'donated'
        return True
        
    def cancel(self):
        for record in self:
                record.state = 'expired'
        return True