from odoo import models,fields
class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Property Offer"

    price = fields.Float()
    property_id = fields.Many2one("estate.property", string="Property", ondelete="cascade")
