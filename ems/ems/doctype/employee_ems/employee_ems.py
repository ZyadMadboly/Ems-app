# Copyright (c) 2024, zeiad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re
from datetime import datetime


class EmployeeEms(Document):
    @frappe.whitelist()
    def validate(self):
         self.validate_fields()
  
    
    def validate_fields(self):
        if not self.employee_name:
            frappe.throw("Please Enter Employee Name")
        if not self.mobile_number:
            frappe.throw("Please Enter Mobile Number")
        else: 
            mobile_no_format = re.match(r'/^(\+2?01)d{9}$/',self.mobile_number)
            if not mobile_no_format:
                frappe.throw("Please Enter Valid Format For The Mobile Number")
        if not self.email_address:
            frappe.throw("Please Enter Email Address")
        else:
            email_format = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.email_address)
            if not email_format:
                frappe.throw("You Have Entered Invalid Format For Email Address")
        if not self.company:
            frappe.throw("Please Choose Company")
        if not self.department:
            frappe.throw("Please Choose Department")
         
        if not self.address:
            frappe.throw("Please Enter Address")
        if not self.designation:
            frappe.throw("Please Enter Your Designation")
            
            
    @frappe.whitelist()
    def calculate_days_at_company(self):
        if not self.days_employed:
            if self.workflow_state == "Hired" and self.hired_on:
                today = datetime.now().date()
                days_employed = (today - self.hired_on).days
                self.days_employed = days_employed
            else:
                self.days_employed = 0

            
   


