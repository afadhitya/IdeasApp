# -*- coding: utf-8 -*-#
from odoo import models, fields, api
from datetime import datetime
from datetime import timedelta
import logging	

class VoteApp(models.Model):
	_name = 'vote.app'
	_description = 'Vote Application'
	_inherit = ['mail.thread']

	name = fields.Char('Title', required=True)
	employee_ids = fields.Many2one('res.users', string='Employee', track_visibility='onchange', default=lambda self: self.env.user,readonly=True)
	date_create = fields.Date(string='Create Date', default=datetime.now())
	company_id = fields.Many2one('res.company', 'Company')
	department_id = fields.Many2one('hr.department', string='Department')
	date_deadline = fields.Date(string='Deadline',default=datetime.now() + timedelta(days=14), required=True)
	idea_id = fields.Many2one('idea.type',string='Idea Type')
	description = fields.Text('Notes',required=True)
	vote_list = fields.One2many('wizard.vote','ideas_id',string='Employee Votes')
	state = fields.Selection([
        ('new', 'New'),
        ('waiting', 'Waiting for Approval'),
        ('approved', 'Approved'),
        ('closed', 'Closed'),
        ('reject', 'Reject'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='new')
	total_vote = fields.Integer(compute='_compute_total_vote', string='Total Vote')

	@api.one
	def do_approve(self):
		self.write({'state': 'approved'})
		return True

	@api.one
	def do_reject(self):
		self.write({'state': 'reject'})
		return True

	@api.one
	def do_post_idea(self):
		self.write({'state': 'waiting'})
		return True

	@api.multi
	def vote_wizard(self):
		_logger = logging.getLogger(__name__)
		_logger.debug('ID:'+ str(self.id))
		return {
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'wizard.vote',
			'target': 'new',
			'type': 'ir.actions.act_window',
			'context': {'current_id': self.id},
		}
	@api.one
	def do_closed(self):
		self.write({'state': 'closed'})
		return True

	@api.multi
	def _compute_total_vote(self):
		for vote in self:
			vote.total_vote = len(vote.vote_list)

	@api.multi
	def action_quotation_send(self):
		''' Pop Up Compose Email '''
		self.ensure_one()
		ir_model_data = self.env['ir.model.data']
		try:
			template_id = ir_model_data.get_object_reference('sale','email_template_edi_sale')[1]
		except ValueError:
			template_id = False

		try:
			compose_form_id = ir_model_data.get_object_reference('mail','email_compose_message_wizard_form')[1]
		except ValueError:
			compose_form_id = False

		ctx = dict()
		ctx.update({
			'default_model':'vote.app',
			'default_res_id': self.ids[0],
			'default_use_template': bool(template_id),
			'default_template_id': template_id,
			'default_composition_mode': 'comment',
			'mark_so_as_sent': True,
			'custom_layout': "sale.mail_template_data_notification_email_sale_order"

			})

		return{
			'type':'ir.actions.act_window',
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'mail.compose.message',
			'views':[(compose_form_id,'form')],
			'view_id': compose_form_id,
			'target':'new',
			'context': ctx,
		}