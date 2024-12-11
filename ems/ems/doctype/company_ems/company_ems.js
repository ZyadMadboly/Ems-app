// Copyright (c) 2024, zeiad and contributors
// For license information, please see license.txt

frappe.ui.form.on("Company Ems", {
    refresh: function(frm) {
        // Calculate departments
        frappe.call({
            method: "calculate_no_of_departments",
            callback: function(response) {
                if (response.message) {
                    frm.refresh_field('no_of_departments');
                }
            }
        });

        // Calculate employees
        frappe.call({
            method: "calculate_no_of_employees",
            callback: function(response) {
                if (response.message) {
                    frm.refresh_field('no_of_employees');
                }
            }
        });
    }
});

