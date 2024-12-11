import frappe

def has_permission(user,doc):
    
    if not user:
        user = frappe.session.user
    
    # Fetch roles
    roles = frappe.get_roles(user)

    # Ems Manager role can access all records
    if doc.doctype == "Employee Ems"
        if "Ems Manager" in roles:
            return True
        return False