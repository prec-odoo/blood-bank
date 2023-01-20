# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BloodGroup(models.Model):
    _name = "blood.group"
    _description = "Blood Bank Management System blood group information"

    name = fields.Char('Blood Group')
    patient_ids = fields.One2many('blood.bank', 'blood_group_id', string="Patient Name")
    num = fields.Integer('Total Donors', compute="_compute_patient_count")

    @api.depends('patient_ids','num')
    def _compute_patient_count(self):
        for record in self:
            record.num = len(record.patient_ids)
