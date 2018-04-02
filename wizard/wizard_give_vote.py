from odoo import tools, api, fields, models

AVAILABLE_PRIORITIES = [
	('1', 'Very Low'),
	('2', 'Low'),
	('3', 'Normal'),
	('4', 'High'),
	('5', 'Very High'),
	('6', 'Most High'),	
]

class open_wizard_vote(models.TransientModel):
	_name = 'wizard.vote'

	priority = fields.Selection(AVAILABLE_PRIORITIES, string='Rating')
	comment = fields.Text('Your Comment', required=True)

	@api.multi
	def button_save(self):
		return True