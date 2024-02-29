# Copyright (c) 2024, Bantoo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MortalityEntry(Document):
	@frappe.whitelist()
	def update_fields(self):		
		self.update_mortality_total()

	def update_mortality_total(self):
		total = 0
		for m in self.mortalities:
			if not m.qty:
				continue
			total = total + m.qty
		self.total_mortalities = total
