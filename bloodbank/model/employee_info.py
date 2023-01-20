# -*- coding: utf-8 -*-

from odoo import models, fields

class EmployeeInfo(models.Model):
    _name = "employee.info"
    _description = "Blood Bank Management System employee information"

    name = fields.Char('Name',required=True)
    