from odoo import tools, api, fields, models

AVAILABLE_PRIORITIES = [
	('0', 'Very Low'),
	('1', 'Low'),
	('2', 'Normal'),
	('3', 'High'),
	('4', 'Very High'),
]

class open_wizard_vote(models.TransientModel):
	_name = 'wizard.vote'

	priority = fields.Selection(AVAILABLE_PRIORITIES, string='Rating')
	comment = fields.Text('Your Comment')

	@api.multi
	def button_save(self):
		return True