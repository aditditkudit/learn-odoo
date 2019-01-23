from odoo import api, fields, models


class Course(models.Model):
    _name = 'academic.course'
    _rec_name ='name'
    _description = 'New Description'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description', required=False, )
    responsible_id = fields.Many2one(comodel_name='res.users', string='Responsible')

    #Object field ini harus punya model academic.session
    session_ids = fields.One2many(comodel_name='academic.session', inverse_name='course_id', string='Sessions', required=False, ondelete="cascade")
    
    
    
