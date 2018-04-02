from odoo import models, fields, api

class IdeaType(models.Model):
	_name = 'idea.type'
	_description = 'Idea Type'
	_inherit = ['mail.thread']
	_order = "name"

	name = fields.Char('Name', required=True)
	min_vote = fields.Integer(string='Minimum Vote',required=True)
	max_vote = fields.Integer(string='Maximum Vote',required=True)
	total_ideas = fields.Integer(string='Total Ideas',required=True)
	department_list = fields.Many2many('hr.department')