frappe.ui.form.on("Purchase Invoice", {
    setup: function(frm){
        frm.set_query("purchase_expense_account", function(doc) {
			return {
				filters: {
                    "root_type":"Expense",
                    "is_group":false
                }
			};
		});
    }
})