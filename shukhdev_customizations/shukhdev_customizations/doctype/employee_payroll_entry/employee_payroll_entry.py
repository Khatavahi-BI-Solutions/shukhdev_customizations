# Copyright (c) 2023, Jigar Tarpara and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class EmployeePayrollEntry(Document):
	@frappe.whitelist()
	def create_payroll_entry(self):
		for row in self.payroll_payable_table:
			self._create_payroll_entry(row)
	
	def _create_payroll_entry(self, row):
		payroll_entry = frappe.new_doc("Payroll Entry")
		payroll_entry.posting_date = self.posting_date
		payroll_entry.payroll_frequency = self.payroll_frequency
		payroll_entry.company = self.company
		payroll_entry.currency = self.currency
		payroll_entry.start_date = self.start_date
		payroll_entry.end_date = self.end_date
		payroll_entry.payroll_payable_account = row.account
		payroll_entry.exchange_rate = 1
		payroll_entry.fill_employee_details()
		payroll_entry.save()
		try:
			payroll_entry.submit()
		except:
			pass
