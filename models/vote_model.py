# -*- coding: utf-8 -*-#
from odoo import models, fields, api
class VoteApp(models.Model):
	_name = 'vote.app'
	_description = 'Vote Application'
	_inherit = ['mail.thread']

	name = fields.Char('Title', required=True)
	employee_ids = fields.Many2one('hr.employee', string='Employee', track_visibility='onchange')
	date_create = fields.Date('Create Date')
	company_id = fields.Many2one('res.company', 'Company')
	department_id = fields.Many2one('hr.department', string='Department')
	date_deadline = fields.Date('Deadline', required=True)
	idea_id = fields.Many2one('idea.type',string='Idea Type')
	description = fields.Text('Notes',required=True)
	vote_list = fields.Many2many('wizard.vote')
	state = fields.Selection([
        ('new', 'New'),
        ('waiting', 'Waiting for Approval'),
        ('approved', 'Approved'),
        ('closed', 'Closed'),
        ('reject', 'Reject'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='new')


	@api.multi
	def do_approve(self):
		self.write({'state': 'approved'})
		return True

		
	@api.multi
	def do_reject(self):
		self.write({'state': 'reject'})
		return True

	@api.multi
	def do_post_idea(self):
		self.write({'state': 'waiting'})
		return True

	@api.multi
	def do_give_vote(self):
		return True

	@api.multi
	def do_closed(self):
		self.write({'state': 'closed'})
		return True