import os
import requests
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

ACCESS_TOKEN = os.getenv("HUBSPOT_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise ValueError("Error: HUBSPOT_ACCESS_TOKEN is not set in the environment or .env file.")

# Set up standard headers for HubSpot API v3
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def test_connection():
    # A simple GET request to list contacts to verify authentication
    url = "https://api.hubapi.com/crm/v3/objects/contacts?limit=1"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        print("Successfully authenticated with HubSpot API!")
        print(response.json())
    else:
        print(f"Authentication failed with status code {response.status_code}:")
        print(response.text)

def get_records(object_type):
    """Fetches records for a given CRM object type (contacts, companies, deals)[cite: 1]."""
    url = f"https://api.hubapi.com/crm/v3/objects/{object_type}?limit=10"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        print(f"\n--- {object_type.upper()} ---")
        for record in data.get("results", []):
            print(f"ID: {record['id']} | Properties: {record.get('properties', {})}")
        return data.get("results", [])
    else:
        print(f"Failed to fetch {object_type}: {response.status_code} - {response.text}")
        return []

def associate_contact_to_company(contact_id, company_id):
    """Programmatically associates a contact with a company using HubSpot v3 batch API[cite: 1]."""
    url = "https://api.hubapi.com/crm/v3/associations/contacts/companies/batch/create"
    payload = {
        "inputs": [
            {
                "from": {"id": contact_id},
                "to": {"id": company_id},
                "type": "contact_to_company"
            }
        ]
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    
    if response.status_code in [200, 201]:
        print("Successfully associated Contact with Company!")
        print(response.json())
    else:
        print(f"Failed to associate contact to company: {response.status_code} - {response.text}")

def associate_contact_to_deal(contact_id, deal_id):
    """Programmatically associates a contact with a deal using HubSpot v3 batch API[cite: 1]."""
    url = "https://api.hubapi.com/crm/v3/associations/contacts/deals/batch/create"
    payload = {
        "inputs": [
            {
                "from": {"id": contact_id},
                "to": {"id": deal_id},
                "type": "contact_to_deal"
            }
        ]
    }
    response = requests.post(url, headers=HEADERS, json=payload)
    
    if response.status_code in [200, 201]:
        print("Successfully associated Contact with Deal!")
        print(response.json())
    else:
        print(f"Failed to associate contact to deal: {response.status_code} - {response.text}")

def verify_associations(contact_id):
    """Verifies associated companies and records for a given contact via API[cite: 1]."""
    specific_url = f"https://api.hubapi.com/crm/v4/objects/contacts/{contact_id}/associations/companies"
    spec_response = requests.get(specific_url, headers=HEADERS)
    
    if spec_response.status_code == 200:
        print(f"\n--- Association Verification for Contact {contact_id} ---")
        print(spec_response.json())
    else:
        print(f"Failed to verify associations: {spec_response.status_code} - {spec_response.text}")

if __name__ == "__main__":
    # 1. Test connection and list available IDs
    test_connection()
    get_records("contacts")
    get_records("companies")
    get_records("deals")
    
    # 2. Define target IDs for association (e.g., Arthur Morgan, Google, Ads?)
    CONTACT_ID = "216689442711"
    COMPANY_ID = "54089353120"
    DEAL_ID = "59277488397"
    
    # 3. Execute associations programmatically[cite: 1]
    associate_contact_to_company(CONTACT_ID, COMPANY_ID)
    associate_contact_to_deal(CONTACT_ID, DEAL_ID)
    
    # 4. Verify the results[cite: 1]
    verify_associations(CONTACT_ID)