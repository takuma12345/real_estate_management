from odoo import models, fields

class Client(models.Model):
    _name = 'real_estate.client'
    _description = 'Client Immobilier'

    name = fields.Char(string='Nom', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Téléphone')
    address = fields.Text(string='Adresse')
