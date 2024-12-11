# Copyright (c) 2024, zeiad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DepartmentEms(Document):
    @frappe.whitelist()
    def validate(self):
        self.validate_fields()
        
        
    
    
 
 
    def validate_fields(self):
        if not self.company:
            frappe.throw("Please Enter Company")
        if not self.department_name:
            frappe.throw("Please Enter Department Name")
        if not self.no_of_employees:
            frappe.throw("Please Enter Number Of Employees")
   
    @frappe.whitelist()
    def calculate_no_of_employees(self):
        num_of_employees = frappe.db.sql("""
                                       select ifnull(count(employee_name),0)
                                       from `tabEmployee Ems` emp_ems
                                       where emp_ems.department = {department}
                                       """.format(department=self.department_name))[0][0]
        self.no_of_employees = num_of_employees
        
        
    