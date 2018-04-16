from odoo import models, fields, api
import logging

class IdeaType(models.Model):
	_name = 'idea.type'
	_description = 'Idea Type'
	_inherit = ['mail.thread']
	_order = "name"

	name = fields.Char('Name', required=True)
	min_vote = fields.Integer(string='Minimum Vote',compute='_vote_count_max_min',readonly=True)
	max_vote = fields.Integer(string='Maximum Vote',compute='_vote_count_max_min',readonly=True)
	total_ideas = fields.Integer(compute='_compute_total_type_idea', string='Total Ideas', readonly=True)
	
	department_list = fields.Many2many('hr.department')
	idea_type = fields.One2many(comodel_name='vote.app', inverse_name='idea_id', string='Idea Type')

	@api.multi
	def _compute_total_type_idea(self):
		for tipe in self:
			tipe.total_ideas = len(tipe.idea_type)


	@api.one
	def _vote_count_max_min(self):
		_logger = logging.getLogger(__name__)
		ideas = self.env['vote.app'].search([('idea_id','=', self.id)])
		min = 0
		max = 0
		i=0
		for idea in ideas:
			num_vote = len(self.env['wizard.vote'].search([('ideas_id','=', idea.id)]))
			if i == 0 or num_vote<min:
				min = num_vote
			if i == 0 or num_vote>max:
				max = num_vote
			_logger.debug("MASUK: " + str(num_vote))
			i = i + 1

		self.min_vote = min
		self.max_vote = max