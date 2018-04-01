# -*- coding: utf-8 -*-#
from odoo import models, fields, api
class VoteApp(models.Model):
	_name = 'vote.app'
	_description = 'Vote Application'
	_inherit = ['mail.thread']


	name = fields.Char('Title', required=True)
	employee_ids = fields.Many2one('res.users','Employee')
	date_create = fields.Date('Create Date')
	company_id = fields.Many2one('res.company', 'Company')
	department_id = fields.Many2one('hr.department', string='Department')
	date_deadline = fields.Date('Deadline', required=True)
	idea_id = fields.Many2one('idea.type',string='Idea Type')
	description = fields.Text('Notes',required=True)
	state = fields.Selection([
        ('new', 'New'),
        ('waiting', 'Waiting for Approval'),
        ('approved', 'Approved'),
        ('closed', 'Closed'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='new')

	@api.multi
	def do_approve(self):
		return True

		
	@api.multi
	def do_reject(self):
		return True

class IdeaType(models.Model):
	_name = 'idea.type'
	_description = 'Idea Type'
	_inherit = ['mail.thread']
	_order = "name"

	name = fields.Char('Name', required=True)
	min_vote = fields.Integer(string='Minimum Vote',required=True)
	max_vote = fields.Integer(string='Maximum Vote',required=True)
	total_ideas = fields.Integer(string='Total Ideas',required=True)