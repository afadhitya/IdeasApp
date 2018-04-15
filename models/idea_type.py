from odoo import models, fields, api

class IdeaType(models.Model):
	_name = 'idea.type'
	_description = 'Idea Type'
	_inherit = ['mail.thread']
	_order = "name"

	name = fields.Char('Name', required=True)
	min_vote = fields.Integer(string='Minimum Vote', readonly=True)
	max_vote = fields.Integer(string='Maximum Vote', readonly=True)
	total_ideas = fields.Integer(compute='_compute_total_type_idea', string='Total Ideas', readonly=True)
	department_list = fields.Many2many('hr.department')

	idea_type = fields.One2many(comodel_name='vote.app', inverse_name='idea_id', string='Idea Type')

	@api.multi
	def _compute_total_type_idea(self):
		for tipe in self:
			tipe.total_ideas = len(tipe.idea_type)
			