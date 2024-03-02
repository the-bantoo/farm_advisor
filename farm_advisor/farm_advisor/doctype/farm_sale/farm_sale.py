# Copyright (c) 2024, Bantoo and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FarmSale(Document):
	@frappe.whitelist()
	def update_fields(self):		
		self.update_item_amount()
		self.update_sales_total()
		self.update_expense_total()
		self.update_deposit_amt()
	
	def update_deposit_amt(self):
		self.amount_to_deposit = self.total - self.total_expenses

	def update_expense_total(self):
		expense_total = 0
		for expense in self.daily_expenses:
			if not expense.amount:
				continue
			expense_total = expense_total + expense.amount
		self.total_expenses = expense_total

	def update_item_amount(self):
		for item in self.sales_items:
			if not item.quantity or not item.price:
				continue
			item.amount = item.quantity * item.price

	def update_sales_total(self):
		total_sales = 0
		for si in self.sales_items:
			if not si.amount:
				continue
			total_sales = total_sales + si.amount

		self.total = total_sales
		


