from odoo import api, fields, models


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    

    is_instructor = fields.Boolean(string='Is Instructor', )
    