# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "makwiz_salary_report"
app_title = "Salary Report"
app_publisher = "MAKWIZ TECHNOLOGIES"
app_description = "Custom Salary Report"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "kmodi@makwiz.com"
app_license = "MIT"

required_apps = ["erpnext"]
fixtures = ["Custom Field", "Property Setter"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/makwiz_salary_report/css/makwiz_salary_report.css"
# app_include_js = "/assets/makwiz_salary_report/js/makwiz_salary_report.js"

# include js, css files in header of web template
# web_include_css = "/assets/makwiz_salary_report/css/makwiz_salary_report.css"
# web_include_js = "/assets/makwiz_salary_report/js/makwiz_salary_report.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "makwiz_salary_report.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "makwiz_salary_report.install.before_install"
# after_install = "makwiz_salary_report.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "makwiz_salary_report.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Salary Slip": {
		"before_insert": "makwiz_salary_report.hooks_call.salary_slip.update_statistical_component_before_insert",
		"after_insert": "makwiz_salary_report.hooks_call.salary_slip.update_statistical_component_after_insert"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"makwiz_salary_report.tasks.all"
# 	],
# 	"daily": [
# 		"makwiz_salary_report.tasks.daily"
# 	],
# 	"hourly": [
# 		"makwiz_salary_report.tasks.hourly"
# 	],
# 	"weekly": [
# 		"makwiz_salary_report.tasks.weekly"
# 	]
# 	"monthly": [
# 		"makwiz_salary_report.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "makwiz_salary_report.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "makwiz_salary_report.event.get_events"
# }

