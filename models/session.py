from odoo import api, fields, models


class Session(models.Model):
    _name = 'academic.session'

    name = fields.Char(string='Name', required=True)

    course_id = fields.Many2one(comodel_name='academic.course', string='Course', required=True)
    instructor_id = fields.Many2one(comodel_name='res.partner', string='Instructor', required=True)
    start_date = fields.Date(string='Start Date', required=False)
    duration = fields.Integer(string='Duration', required=False)
    seats = fields.Integer(string='Seats', required=False)
    active = fields.Boolean(string='Active')
    
    
    
    
    
    
