{
    'name': 'Clinique veterinaire',
    'version': '1.0',
    'summary': 'Gestion d\'une file d\'animaux',
    'category': 'Services',
    'author': 'Manel Guechetouli',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/animal_view.xml",
    ],
    'installable': True,
    'application': True,
}
