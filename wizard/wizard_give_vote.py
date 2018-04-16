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
		#_logger.debug('CONTEXT ID:'+ str(self.id))

		resource = self.env['resource.resource'].search([('user_id','=', self.env.uid)])[0]
		employee = self.env['hr.employee'].search([('resource_id','=', resource.id)])[0]

		_logger.debug('RESOURCE ID: ' + str(employee.name_related))
		return self.env['vote.app'].browse(self._context.get('current_id', 1))

	@api.model
	def _current_employee(self):

		resource = self.env['resource.resource'].search([('user_id','=', self.env.uid)])[0]
		employee = self.env['hr.employee'].search([('resource_id','=', resource.id)])[0]

		_logger = logging.getLogger(__name__)
		_logger.debug('RESOURCE ID: ' + str(employee.name_related))
		return employee.id

	@api.model
	def _current_department(self):

		resource = self.env['resource.resource'].search([('user_id','=', self.env.uid)])[0]
		employee = self.env['hr.employee'].search([('resource_id','=', resource.id)])[0]

		_logger = logging.getLogger(__name__)
		_logger.debug('RESOURCE ID: ' + str(employee.name_related))
		return employee.department_id

	#Field
	ideas_id = fields.Many2one('vote.app', string="Ideas", required=True, default=_current_id, readonly=True)
	department = fields.Many2one('hr.department', string="Department", required=True, default=_current_department, readonly=True)
	employee = fields.Many2one('hr.employee', string="Employee", required=True, default=_current_employee, readonly=True)

	priority = fields.Selection(AVAILABLE_PRIORITIES, string='Rating')
	comment = fields.Text('Your Comment', required=True)

	@api.multi
	def button_save(self):
		return True