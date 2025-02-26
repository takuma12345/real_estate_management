from odoo import models, fields

class Contract(models.Model):
    _name = 'real_estate.contract'
    _description = 'Contrat Immobilier'

    name = fields.Char(string='Référence', required=True)
    property_id = fields.Many2one('real_estate.property', string='Propriété')
    client_id = fields.Many2one('real_estate.client', string='Client')
    start_date = fields.Date(string='Date de début')
    end_date = fields.Date(string='Date de fin')
    rent = fields.Float(string='Loyer')
