# HubSpot API Record Association Task

This project demonstrates how to manually and programmatically associate CRM records (**Contacts**, **Companies**, and **Deals**) in HubSpot using both the HubSpot user interface and the HubSpot v3/v4 APIs[cite: 1].

## Scenario
As part of managing client relationships for **CloudSync Solutions**, this script automates the process of linking contacts to their respective corporate accounts and deals to ensure smooth sales tracking and reporting[cite: 1].

## Features
* **Environment Security**: Uses `python-dotenv` to manage credentials securely and prevent token leaks.
* **Record Discovery**: Automatically fetches and logs record IDs for contacts, companies, and deals from your portal[cite: 1].
* **Programmatic Association**: Links contacts to companies and deals using HubSpot's v3 batch association endpoints[cite: 1].
* **Verification**: Confirms relationship status via API queries[cite: 1].

## Project Structure
* `association_manager.py`: Main script containing connection tests, ID fetching logic, association requests, and verification checks.
* `.env`: Local environment variables file storing your Private App Token (**ignored by Git**).
* `.gitignore`: Ensures sensitive files and local caches are never committed to version control.

## Setup Instructions

### 1. Install Dependencies
Make sure you have `requests` and `python-dotenv` installed. Run the following command in your terminal:

```bash
pip install requests python-dotenv
```

### 2. Configure Environment Variables
Create a `.env` file in the root directory of your project and add your HubSpot Private App Token:

```env
HUBSPOT_ACCESS_TOKEN=your_actual_token_here
```

### 3. Run the Script
Once your dependencies are installed and the environment is configured, execute the script:

```bash
python association_manager.py
```