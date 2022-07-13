from __future__ import unicode_literals
import frappe
from frappe.utils import flt, cstr, cint
from frappe import msgprint, _

@frappe.whitelist(allow_guest=True)
def update_statistical_component_before_insert(self, method):
	component_type_name = frappe.db.get_value("Pre Payroll", None, "component_type")
	if not component_type_name:
		frappe.throw(("Establecer Pre Payroll"))
	frappe.db.sql("""update `tabEmployee` set makwiz_component_type=%s 
				where name=%s""", (component_type_name, self.employee))	

@frappe.whitelist(allow_guest=True)
def update_statistical_component_after_insert(self, method):	
	frappe.db.sql("""update `tabEmployee` set makwiz_component_type=%s 
				where name=%s""", ("", self.employee))	