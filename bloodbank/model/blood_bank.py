# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError
from odoo.tools.date_utils import add
from datetime import timedelta

class BloodBank(models.Model):
    _name = "blood.bank"
    _description = "Blood Bank Management System"
    _inherit = ['mail.thread','mail.activity.mixin'] #to add the chatter 

    availability_date = fields.Date('Availability Date',required=True,default=lambda self:fields.Datetime.now())
    name = fields.Char('Name',required=True)
    contact = fields.Char('Contact No.')
    date_of_birth = fields.Date('Birth Date',default=lambda self:fields.Datetime.now())
    age = fields.Integer('Age', compute='_compute_age')
    doctor_info_id = fields.Many2one('doctor.info', string='Doctor Name', tracking=True)
    employee_info_id = fields.Many2one('employee.info', string='Employee Name', tracking=True)
    blood_group_id = fields.Many2one('blood.group', string='Blood Group', tracking=True)
    issue_ids = fields.Many2many("medical.issue", string="Medical Issues")
    email = fields.Char('Email')
    validity = fields.Date('Valid Till', compute ='_compute_validity')
    address = fields.Char('Address')
    bag_number = fields.Char('Bag Number',copy=False)
    quantity = fields.Integer('Quantity', tracking=True)
    active = fields.Boolean(default=True)
    # image = fields.Image()
    gender = fields.Selection(
        string='Gender',
        selection=[('male','Male'),('female','Female'),('other','Other')],
    )
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('available', 'Available'),('donated', 'Donated'), ('expired', 'Expired'), ('cancelled', 'Cancelled')],
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

    @api.ondelete(at_uninstall=False)
    def _unlink_if_not_new_or_available(self):
        for record in self:
            if record.state in ['new', 'available']:
                raise UserError("New and available donors can npt be deleted.")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            record.age = relativedelta(record.availability_date, record.date_of_birth).years
    
    @api.depends('availability_date')
    def _compute_validity(self):
        for record in self:
            record.validity = record.availability_date + timedelta(days = 15)    

    @api.constrains('blood_group_id')
    def _check_blood_group_available(self):
        for record in self:
            if record.blood_group_id:
                record.state = 'available'

    @api.constrains('issue_ids')
    def _check_medical_issue(self):
        for record in self:
            if record.issue_ids.name != 'No issues':
                record.state = 'cancelled'
            else:
                record.state = 'available'
