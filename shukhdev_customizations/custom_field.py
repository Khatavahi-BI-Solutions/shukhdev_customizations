from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def setup_custom_fields():
	custom_fields = {
		"Sales Invoice": [
			dict(fieldname='sales_income_account',
				 label='Income Account',
				 fieldtype='Link',
				 insert_after='update_stock',
				 reqd=1,
				 options='Account'
				 ),
		],
		"Purchase Invoice": [
			dict(fieldname='purchase_expense_account',
				 label='Purchase Expense Account',
				 fieldtype='Link',
				 insert_after='update_stock',
				 reqd=1,
				 options='Account'
				 ),
		]
	}
	try:
		create_custom_fields(custom_fields)
	except:
		print("Exception while createing customfield")