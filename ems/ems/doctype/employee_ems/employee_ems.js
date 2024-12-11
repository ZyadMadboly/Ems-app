// Copyright (c) 2024, zeiad and contributors
// For license information, please see license.txt

frappe.ui.form.on("Employee Ems", {
	refresh(frm) {
        // Ensure that the Department field in Employee modes only accepts departments related to the selected company
        frm.set_query("department", (doc) => {
            return {
                filters: {
                    company: frm.doc.company
                }
            };
        });
	},
    refresh: function(frm) {
        frappe.call({
            method: 'calculate_days_at_company',
            doc: frm.doc,
            callback: function(response) {
                frm.refresh_field('days_employed');
            }
        });
    }
});


