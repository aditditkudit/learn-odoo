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

    attendee_ids = fields.One2many(comodel_name='academic.attendee', inverse_name='session_id', string='Attendees', required=False)

    taken_seats = fields.Float(string='Taken Seat', required=False, compute='_calc_taken_seats')
    
    @api.depends('attendee_ids', 'seats')
    def _calc_taken_seats(self):
        for rec in self:
            if rec.seats > 0:
                rec.taken_seats = 100.0 * len(rec.attendee_ids) / rec.seats
            else:
                rec.taken_seats = 0.0 
    
    @api.onchange('seats')
    def onchange_seats(self):
        if self.seats > 0:
            self.taken_seats = 100.0 * len(self.attendee_ids) / self.seats
        else:
            self.taken_seats = 0.0
    
    @api.multi
    def _cek_instruktur(self):
        # Add code here
        for session in self:
            x = [att.partner_id.id for att in session.attendee_ids]
            if session.instructor_id.id in x:
                return False
            
        return True
    
    _constraints = [(_cek_instruktur, 'Instructor cannot be Attendee',['instructor_id', 'attendee_ids'])]
    

    
    
    
    
    
    
    
