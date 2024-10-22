import os

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()


CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# FatSecret OAuth token endpoint
token_url = "https://oauth.fatsecret.com/connect/token"

# Data required for requesting the token
data = {
    "grant_type": "client_credentials",  # OAuth grant type
    "scope": "basic",  # Scope of access
}


# Function to get the access token
def get_access_token():
    response = requests.post(
        token_url, data=data, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    )
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print("Error getting token:", response.status_code, response.text)
        return None


# Fetch the token
access_token = get_access_token()

# Proceed if the token is successfully retrieved
if access_token:
    # Set the headers with the access token
    headers = {"Authorization": f"Bearer {access_token}"}

    # API endpoint for food search
    search_url = "https://platform.fatsecret.com/rest/server.api"
    params = {
        "method": "foods.search",
        "search_expression": "apple",  # Example search term
        "format": "json",
    }

    # Make the request
    response = requests.get(search_url, headers=headers, params=params)

    # Print the response from the API
    if response.status_code == 200:
        print("Food Search Results:", response.json())
    else:
        print("Error:", response.status_code, response.text)
else:
    print("Failed to retrieve access token.")
