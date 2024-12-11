import requests
import frappe
from requests.exceptions import RequestException

BASE_URL = "http://localhost:8080/api/resource"

headers = {
    'Authorization': 'token 409987067f774e2:ad368f18c8c56b9',
    'Content-Type': 'application/json'
}



@frappe.whitelist()
def test():
    try:
        url = f"{BASE_URL}/company-ems"
        response = requests.get(url, headers=headers, timeout=20)
        return response.json()
    except:
        return "woo"



def handle_api_response(response, method):
    try:
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        error_message = f"API {method} failed: Connection error"
        frappe.log_error(message=str(e), title=error_message)
        return {"error": True, "message": error_message}




@frappe.whitelist(allow_guest=True)
def get_companies():
    try:
        url = f"{BASE_URL}/company-ems"
        response = requests.get(url, headers=headers, timeout=20)
        return handle_api_response(response)
    except RequestException as e:
        frappe.log_error(f"Request failed: {str(e)[:60]}", "API Error")
        return {"error": "Failed to fetch companies"}
    
@frappe.whitelist()
def get_company(name):
    try:
        url = f"{BASE_URL}/company-ems/{name}"
        response = requests.get(url, headers=headers, timeout=20)
        return handle_api_response(response)
    except RequestException as e:
        frappe.log_error(f"Request failed: {str(e)[:60]}", "API Error")
        return {"error": f"Failed to fetch company {name}"}
    
@frappe.whitelist()
def get_departments():
    try:
        url = f"{BASE_URL}/department-ems"
        response = requests.get(url, headers=headers, timeout=20)
        return handle_api_response(response)
    except RequestException as e:
        frappe.log_error(f"Request failed: {str(e)[:60]}", "API Error")
        return {"error": "Failed to fetch departments"}

@frappe.whitelist()
def get_department(name):
    try:
        url = f"{BASE_URL}/department-ems/{name}"
        response = requests.get(url, headers=headers, timeout=20)
        return handle_api_response(response)
    except RequestException as e:
        frappe.log_error(f"Request failed: {str(e)[:60]}", "API Error")
        return {"error": f"Failed to fetch department {name}"}
    
@frappe.whitelist()
def create_employee(data):
    try:
        url = f"{BASE_URL}/employee-ems"
        response = requests.post(url, headers=headers, json=data, timeout=20)
        return handle_api_response(response)
    except RequestException as e:
        frappe.log_error(f"Request failed: {str(e)[:60]}", "API Error")
        return {"error": "Failed to create employee"}
    
@frappe.whitelist()
def get_employees():
    try:
        url = f"{BASE_URL}/employee-ems"
        response = requests.get(url, headers=headers, timeout=20)
        return handle_api_response(response)
    except RequestException as e:
        frappe.log_error(f"Request failed: {str(e)[:60]}", "API Error")
        return {"error": "Failed to fetch employees"}

def get_employee(name):
    try:
        url = f"{BASE_URL}/employee-ems/{name}"
        response = requests.get(url, headers=headers, timeout=20)
        return handle_api_response(response)
    except RequestException as e:
        frappe.log_error(f"Request failed: {str(e)[:60]}", "API Error")
        return {"error": f"Failed to fetch employee {name}"}

def update_employee(name, data):
    try:
        url = f"{BASE_URL}/employee-ems/{name}"
        response = requests.put(url, headers=headers, json=data, timeout=20)
        return handle_api_response(response)
    except RequestException as e:
        frappe.log_error(f"Request failed: {str(e)[:60]}", "API Error")
        return {"error": f"Failed to update employee {name}"}

def delete_employee(name):
    try:
        url = f"{BASE_URL}/employee-ems/{name}"
        response = requests.delete(url, headers=headers, timeout=20)
        return response.status_code
    except RequestException as e:
        frappe.log_error(f"Request failed: {str(e)[:60]}", "API Error")
        return {"error": f"Failed to delete employee {name}"}
