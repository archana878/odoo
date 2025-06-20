from odoo import models,fields

class EstatePropertyTag(models.Model):
    _name='estate.property.tag'
    _description='property tag'

    name=fields.char(required=True)
    