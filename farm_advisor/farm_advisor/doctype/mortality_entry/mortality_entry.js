// Copyright (c) 2024, Bantoo and contributors
// For license information, please see license.txt

frappe.ui.form.on("Mortality Entry", {
	refresh(frm) {

	},
    validate(frm) {
        update_form(frm);
    }
});

function update_form(frm){
	frappe.call({
		method: "update_fields",
		doc: frm.doc,
		callback: () => {
			frm.refresh();
		}
	})
}
