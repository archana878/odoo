from odoo import models,fields
class EstatePropertyoffer(models.Model):
    _name='estate.property.offer'
    _description='Property Offer'

    price = fields.Float(required=True)
    property_id = fields.Many2one('estate.property', string="Property", required=True)
    partner_id = fields.Many2one('res.partner', string="Partner", required=True)