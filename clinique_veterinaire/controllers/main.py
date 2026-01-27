from odoo import http
from odoo.http import request

class CliniqueWebsite(http.Controller):

    #Route pour afficher une page web
    #qui est accessible sans login
    @http.route(
        route ='/clinique/animaux',
        type='http',
        auth='public',
        website=True
    )

    #appelee automatiquement quand quelqu’un va sur l’URL :

    def afficher_animaux(self, **kwargs):
        #Dans l'environnement, cherche mon modele 'clinique.animal'
        #ignore les droits d'acces (sudo)
        #cherche tous les animaux

        ##Comme SELECT * FROM clinique.animal;
        animals = request.env['clinique.animal'].sudo().search([])

        #donnees renvoyees a la page
        return request.render(
            'clinique_veterinaire.website_animaux', #Id du 'template'
            {
                'animals': animals #variable utilisable dans le XML
            }
        )
