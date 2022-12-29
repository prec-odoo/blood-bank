# -*- coding: utf-8 -*-

from odoo import models, fields

class DoctorInfo(models.Model):
    _name = "doctor.info"
    _description = "Blood Bank Management System doctor information"

    name = fields.Char('Name',required=True)