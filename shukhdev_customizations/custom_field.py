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
		]
	}

	create_custom_fields(custom_fields)