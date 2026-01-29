from odoo import fields, models


class CliniqueProprietaire(models.Model):
    _name = "clinique.proprietaire"
    _description = "Proprietaire d'un animal"

    name = fields.Char(string="Nom du proprietaire")
    phone_number = fields.Char(string="Numero de telephone")
    email = fields.Char(string="Courriel")

    animal_ids = fields.One2many(
        "clinique.animal", "proprietaire_id", string="Animaux"
    )


# Represente une liste d'animaux (que possede le proprietaire), comme :
# SELECT * FROM clinique.animal
# WHERE proprietaire_id = ce_proprietaire.id;
