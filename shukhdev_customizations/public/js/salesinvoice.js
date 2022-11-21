frappe.ui.form.on("Sales Invoice", {
    setup: function(frm){
        frm.set_query("sales_income_account", function(doc) {
			return {
				filters: {
                    "root_type":"Income",
                    "is_group":false
                }
			};
		});
    }
})