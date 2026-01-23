from odoo import http
from odoo.http import request

class CliniqueWebsite(http.Controller):

    @http.route(
        '/clinique/animaux',
        type='http',
        auth='public',
        website=True
    )

    def afficher_animaux(self, **kwargs):
        #Dans l'environnement, cherche mon modele 'clinique.animal'
        #ignore les droits d'acces (sudo)
        #cherche tous les animaux

        ##Comme SELECT * FROM clinique.animal;
        animals = request.env['clinique.animal'].sudo().search([])

        #donnees renvoyees a la page
        return request.render(
            'clinique_veterinaire.website_animaux',
            {
                'animals': animals
            }
        )
