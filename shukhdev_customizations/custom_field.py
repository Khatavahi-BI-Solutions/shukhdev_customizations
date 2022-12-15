from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def setup_custom_fields():
	custom_fields = {
		"Sales Invoice": [
			dict(fieldname='set_default_sales_income_account',
				 label='Set Default Sales Income Accouunt',
				 fieldtype='Check',
				 insert_after='update_stock',
				 hidden=0
				 ),
			dict(fieldname='sales_income_account',
				 label='Income Account',
				 fieldtype='Link',
				 insert_after='set_default_sales_income_account',
				 mandatory_depends_on= 'eval:doc.set_default_sales_income_account',
				 depends_on= 'eval:doc.set_default_sales_income_account',
				 options='Account'
				 ),
		],
		"Purchase Invoice": [
			dict(fieldname='purchase_expense_account',
				 label='Purchase Expense Account',
				 fieldtype='Link',
				 insert_after='update_stock',
				 reqd=0,
				 hidden=1,
				 options='Account'
				 ),
			dict(fieldname='ignore_purchase_expense_account',
				 label='Ignore Purchase Expense Account',
				 fieldtype='Check',
				 insert_after='purchase_expense_account',
				 hidden=1
				 ),
			dict(fieldname='bill_file',
				 label='Bill Attachment',
				 fieldtype='Attach',
				 insert_after='posting_time',
				 reqd=1,
				 ),
		],
		"Expense Claim Detail": [
			dict(fieldname='bill_file',
				 label='Bill Attachment',
				 fieldtype='Attach',
				 insert_after='posting_time',
				 reqd=1,
				 in_list_view = 1
				 ),
		]
	}
	try:
		create_custom_fields(custom_fields)
	except:
		print("Exception while createing customfield")