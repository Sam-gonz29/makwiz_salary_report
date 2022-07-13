from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Reports"),
			"icon": "fa fa-list",
			"items": [	
				{
					"type": "report",
					"is_query_report": True,
					"name": "NOMINA",
					"doctype": "Salary Slip"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "CONTRIBUCION EMPLEADOR",
					"doctype": "Salary Slip"
				},
			]
		},

		{
			"label": _("Payroll"),
			"items": [
				{
					"type": "doctype",
					"name": "Pre Payroll",
					"label": _("Pre Payroll"),
					"description":_("set payroll frequency before process payroll"),
					"hide_count": True
				},
			]
		},

	]
