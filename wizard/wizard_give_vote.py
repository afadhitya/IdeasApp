from odoo import tools, api, fields, models
import logging

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

	@api.model
	def _current_id(self):
		_logger = logging.getLogger(__name__)
		_logger.debug('CONTEXT ID:'+ str(self.id))
		return self.env['vote.app'].browse(self._context.get('current_id', 1))

	ideas_id = fields.Many2one('vote.app', string="Ideas", required=True, default=_current_id, readonly=True)
	priority = fields.Selection(AVAILABLE_PRIORITIES, string='Rating')
	comment = fields.Text('Your Comment', required=True)

	@api.multi
	def button_save(self):
		return True