from odoo import api, fields, models


class Attendee(models.Model):
    _name = 'academic.attendee'
    _rec_name ='name'

    name = fields.Char(string='Name')
    session_id = fields.Many2one(comodel_name='academic.session', string='Session', required= False,)
    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner', required=False,)

    
    
