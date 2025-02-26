from odoo import models, fields

class Property(models.Model):
    _name = 'real_estate.property'
    _description = 'Propriété Immobilière'

    name = fields.Char(string='Nom', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Prix')
    living_area = fields.Integer(string='Surface habitable')
    bedrooms = fields.Integer(string='Nombre de chambres')
    bathrooms = fields.Integer(string='Nombre de salles de bain')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Jardin')
    active = fields.Boolean(string='Actif', default=True)
    state = fields.Selection(
        [('available', 'Disponible'), ('sold', 'Vendu')],
        string='État',
        default='available'
    )
