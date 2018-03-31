# -*- coding: utf-8 -*-
from odoo import models, fields, api
class IdeaTask(models.Model):
	_name = 'idea.task'
	_description = 'Idea Task'

	
	name = fields.Char('Title', required=True)
	employee = fields.Char('Employee')
	created = fields.Date('Created')
	company = fields.Char('Company')
	departement = fields.Char('Departement')
	deadline = fields.Date('Deadline',required=True)
	idea_type = fields.Char('Idea Type')