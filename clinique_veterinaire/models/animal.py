from odoo import fields, models

#classe qui represente table dans la BDD
class CliniqueAnimal(models.Model):

    _name = 'clinique.animal'
    _description = 'Animal pour la clinique'

    #comme les "attributs" de ma classe
    #(les colonnes de ma BD)
    name = fields.Char(string="Nom")
    species = fields.Char(string="Espece")
    birth_date = fields.Date(string="Date de naissance")
    sterilized = fields.Selection(
        string="Sterilise",
        selection=[
            ("yes", "Oui"),
            ("no", "Non"),
            ("unknown", "inconnu"),
        ],
        default="unknown",
        required=True,
    )

    proprietaire_id = fields.Many2one("clinique.proprietaire", string="Proprietaire")
    cage_ids = fields.Many2many(
        comodel_name="clinique.cage",
        relation="clinique_animal_cage_relation",
        column1="animal_id",
        column2="cage_id",
        string="Cages"
    )
