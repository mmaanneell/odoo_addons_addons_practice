from odoo import api, fields, models


class CliniqueCage(models.Model):
    _name = "clinique.cage"
    _description = "Cage de la clinique"

    name = fields.Char(string="Description")
    color = fields.Char(string="Couleur")
    size = fields.Selection(
        string="Taille",
        selection=[
            ("small", "Petit"),
            ("medium", "Moyen"),
            ("large", "Grand"),
            ("unknown", "Inconnu"),
        ],
        default="unknown",
        required=True,
    )

    animal_ids = fields.Many2many(
        comodel_name="clinique.animal",
        relation="clinique_animal_cage_relation",
        column1="cage_id",
        column2="animal_id",
        string="Animaux",
    )

    animal_count = fields.Integer(
        compute="_compute_animal_count",
        string="Nombre d'animaux",
        store=False,
    )

    @api.depends("animal_ids")
    def _compute_animal_count(self):
        for cage in self:
            cage.animal_count = len(cage.animal_ids)
