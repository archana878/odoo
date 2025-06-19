from odoo import models,fields

class EstateProperty(models.Model):
    _name='estate.property'
    _discription='estate property'

    name=fields.Char(string="Title",required=True)
    discription=fields.Text()