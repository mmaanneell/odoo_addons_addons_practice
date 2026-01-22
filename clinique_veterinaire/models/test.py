from odoo import fields, models

class CliniqueTest(models.Model):
    _name = 'clinique_test'
    _description = 'Test pour la clinique'

    name = fields.Char(string="Nom")
