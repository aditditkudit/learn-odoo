from odoo import api, fields, models, _

class CreateAttendeeWizard(models.TransientModel):
    _name = 'academic.create.attendee.wizard'

    def _get_active_session(self):
        context = self.env.context
        if context.get('active_model') == 'academic.session':
            return context.get('active_ids', False)
        return False
    
    # nambahin attendee untuk 1 session
    # session_id = fields.Many2one(comodel_name="academic.session", string="Sessions", required=False, default=_get_active_session)

    # nambahin attendee untuk lebih dari 1 session
    session_ids = fields.Many2many(comodel_name='academic.session', string='Sessions')
    

    attendee_ids = fields.One2many(comodel_name="academic.attendee.wizard",
                                   inverse_name="wizard_id", string="Attendees to Add",
                                   required=False, )
    
    # function untuk nambahin attendee untuk 1 session
    # @api.multi
    # def action_add_attendee(self):
    #     self.ensure_one()
    #     session = self.session_id
    #     att_data = [{'partner_id' : att.partner_id.id}
    #                 for att in self.attendee_ids]
    #     session.attendee_ids = [(0, 0, data) for data in att_data]

    #     return {'type': 'ir.actions.act_window_close'}

    # function untuk nambahin attendee untuk lebih dari 1 session
    @api.multi
    def action_add_attendee(self):
        self.ensure_one()
        sessions = self.session_ids
        att_data = [{'partner_id': att.partner_id.id}
            for att in self.attendee_ids]
        
        for session in sessions:
            session.attendee_ids = [(0, 0, data) for data in att_data]
        
        return {'type': 'ir.actions.act_window_close'}

class AttendeeWizard(models.TransientModel):
    _name = 'academic.attendee.wizard'
    
    wizard_id = fields.Many2one(comodel_name="academic.create.attendee.wizard",
                                string="Wizard", required=False, )
    partner_id = fields.Many2one(comodel_name="res.partner",
                                 string="Partner", required=False, )
