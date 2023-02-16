// Copyright (c) 2023, Jigar Tarpara and contributors
// For license information, please see license.txt
var in_progress = false;
frappe.ui.form.on('Employee Payroll Entry', {
	refresh: function (frm) {
		frm.page.clear_primary_action();
		frm.add_custom_button(__("Create Payroll Entry"),
			function () {
				frm.events.create_payroll_entry(frm);
			}
		).toggleClass("btn-primary", false);
	},
	create_payroll_entry: function (frm) {
		return frappe.call({
			doc: frm.doc,
			method: 'create_payroll_entry',
		}).then(r => {
			if (r.docs && r.docs[0].employees) {
				frm.employees = r.docs[0].employees;
				frm.dirty();
				frm.save();
				frm.refresh();
				if (r.docs[0].validate_attendance) {
					render_employee_attendance(frm, r.message);
				}
				frm.scroll_to_field("employees");
			}
		});
	},
	start_date: function (frm) {
		if (!in_progress && frm.doc.start_date) {
			frm.trigger("set_end_date");
		} else {
			// reset flag
			in_progress = false;
		}
		// frm.events.clear_employee_table(frm);
	},
	set_end_date: function (frm) {
		frappe.call({
			method: 'hrms.payroll.doctype.payroll_entry.payroll_entry.get_end_date',
			args: {
				frequency: frm.doc.payroll_frequency,
				start_date: frm.doc.start_date
			},
			callback: function (r) {
				if (r.message) {
					frm.set_value('end_date', r.message.end_date);
				}
			}
		});
	},
	payroll_frequency: function (frm) {
		frm.trigger("set_start_end_dates").then(() => {
			// frm.events.clear_employee_table(frm);
		});
	},
	// clear_employee_table: function (frm) {
	// 	frm.clear_table('employees');
	// 	frm.refresh();
	// },
	set_start_end_dates: function (frm) {
		if (!false) {
			frappe.call({
				method: 'hrms.payroll.doctype.payroll_entry.payroll_entry.get_start_end_dates',
				args: {
					payroll_frequency: frm.doc.payroll_frequency,
					start_date: frm.doc.posting_date
				},
				callback: function (r) {
					if (r.message) {
						in_progress = true;
						frm.set_value('start_date', r.message.start_date);
						frm.set_value('end_date', r.message.end_date);
					}
				}
			});
		}
	},
	currency: function (frm) {
		var company_currency;
		if (!frm.doc.company) {
			company_currency = erpnext.get_currency(frappe.defaults.get_default("Company"));
		} else {
			company_currency = erpnext.get_currency(frm.doc.company);
		}
		if (frm.doc.currency) {
			if (company_currency != frm.doc.currency) {
				frappe.call({
					method: "erpnext.setup.utils.get_exchange_rate",
					args: {
						from_currency: frm.doc.currency,
						to_currency: company_currency,
					},
					callback: function (r) {
						frm.set_value("exchange_rate", flt(r.message));
						frm.set_df_property('exchange_rate', 'hidden', 0);
						frm.set_df_property("exchange_rate", "description", "1 " + frm.doc.currency +
							" = [?] " + company_currency);
					}
				});
			} else {
				frm.set_value("exchange_rate", 1.0);
				frm.set_df_property('exchange_rate', 'hidden', 1);
				frm.set_df_property("exchange_rate", "description", "");
			}
		}
	},
	setup: function (frm) {
		frm.set_query('account', 'payroll_payable_table', function () {
			return {
				filters: {
					"company": frm.doc.company,
					"root_type": "Liability",
					"is_group": 0,
				}
			};
		});

	}
});
