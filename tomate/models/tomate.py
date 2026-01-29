from odoo import _, api, fields, models


class Tomate(models.Model):
    _name = "tomate"
    _description = "tomate"
    _order = "id"

    name = fields.Char()

    poids = fields.Float()
