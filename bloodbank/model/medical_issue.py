# -*- coding: utf-8 -*-

from odoo import models, fields

class MedicalIssue(models.Model):
    _name = "medical.issue"
    _description = "Blood Bank Management System medical issues"

    name = fields.Char('Name',required=True)
    color = fields.Integer()
    