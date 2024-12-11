# Copyright (c) 2024, zeiad and contributors
# For license information, please see license.txt

from frappe.model.document import Document
import frappe
import re

class UserAccounts(Document):

    @frappe.whitelist()
    def validate(self):
        self.validate_fields()

    def validate_fields(self):
        if not self.user_name:
            frappe.throw("Please Enter User Name")
        if not self.email_address:
            frappe.throw("Please Enter Email Address")
        else:
            email_format = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email_address)
            if not email_format:
                frappe.throw("You Have Entered Invalid Format For Email Address")
        if not self.role:
            frappe.throw("Please Enter Role")

    