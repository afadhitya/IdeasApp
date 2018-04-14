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
	employee_ids = fields.Many2one('hr.employee', string='Employee', track_visibility='onchange')
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