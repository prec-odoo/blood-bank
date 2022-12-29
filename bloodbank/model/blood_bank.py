# -*- coding: utf-8 -*-

from odoo import models, fields

class BloodBank(models.Model):
    _name = "blood.bank"
    _description = "Blood Bank Management System"

    date = fields.Date('Registration Date',required=True)
    name = fields.Char('Name',required=True)
    contact = fields.Char('Contact No.')
    bdate = fields.Date('Birth Date')
    email = fields.Char('Email')
    address = fields.Char('Address')
    description = fields.Text('Details',copy=False)
    gender = fields.Selection(
        string='Gender',
        selection=[('male','Male'),('female','Female')],
    )
    b_group = fields.Selection(
        string='Blood Group',
        selection=[('ap','A+'),('bp','B+'),('an','A-'),('bn','B-'),('op','O+'),('on','O-'),('abp','AB+'),('abn','AB-')],
    )