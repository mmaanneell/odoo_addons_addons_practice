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

    proprietaire_id = fields.Many2one("clinique.proprietaire", string="Proprietaire")
