{
	'name':'Vote Application',
	'description': 'Manage your Voting.',
	'author': 'KELOMPOK B2',
	'depends': ['base','mail','hr'],
	'data': [
		'security/vote_security.xml',
		'security/ir.model.access.csv',
		'views/vote_menu.xml',
		'views/vote_view.xml',
		'views/idea_type_view.xml',
		'reports/report_vote.xml',
		'reports/report_vote_template.xml'
	],
	'application': True,
}
