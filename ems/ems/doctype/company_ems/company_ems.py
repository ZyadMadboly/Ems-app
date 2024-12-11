# Copyright (c) 2024, zeiad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CompanyEms(Document):
    @frappe.whitelist()
    def validate(self):
        self.validate_fields()
        self.calculate_no_of_departments()
        self.calculate_no_of_employees()

    def validate_fields(self):
        if not self.company_name:
            frappe.throw("Please Enter Company Name")
        if not self.no_of_departments:
            frappe.throw("Please Enter Numner Of Departments")
        if not self.no_of_employees:
            frappe.throw("Please Enter Number Of Employees")
   
@frappe.whitelist()
def calculate_no_of_departments(self):
    num_of_departs = frappe.db.sql("""
        select ifnull(count(department_name),0)
        from `tabDepartment Ems` dep_ems
        where dep_ems.company = {company}
    """.format(company=self.company_name))[0][0]
    
    self.no_of_departments = num_of_departs

@frappe.whitelist()
def calculate_no_of_employees(self):
    num_of_employees = frappe.db.sql("""
        select ifnull(count(employee_name),0)
        from `tabEmployee Ems` emp_ems
        where emp_ems.company = %(company)s
    """.format(company=self.company_name))[0][0]
    
    self.no_of_employees = num_of_employees
