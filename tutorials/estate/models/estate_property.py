from odoo import models,fields
class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Property"

    name = fields.Char(required=True)
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    buyer_id = fields.Many2one("res.partner", string="Buyer")
    salesperson_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
