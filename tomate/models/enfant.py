from odoo import _, api, fields, models


class Enfant(models.Model):
    _name = "enfant"
    _description = "enfant"
    _order = "id"

    name = fields.Char()

    manger = fields.Many2one(comodel_name="tomate")
