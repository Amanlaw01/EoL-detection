import requests
import json

# Banner
print("""
 ________    ___   _____      ______           _                 _    _                   
|_   __  | .'   `.|_   _|    |_   _ `.        / |_              / |_ (_)                  
  | |_ \_|/  .-.  \ | |        | | `. \ .---.`| |-'.---.  .---.`| |-'__   .--.   _ .--.   
  |  _| _ | |   | | | |   _    | |  | |/ /__\\| | / /__\\/ /'`\]| | [  |/ .'`\ \[ `.-. |  
 _| |__/ |\  `-'  /_| |__/ |  _| |_.' /| \__.,| |,| \__.,| \__. | |, | || \__. | | | | |  
|________| `.___.'|________| |______.'  '.__.'\__/ '.__.''.___.'\__/[___]'.__.' [___||__] 
""")

# Author information
print("Author: SpongyYeti")

# Set the API endpoint
api_endpoint = "https://endoflife.date/api"

# Get the input service from the user
input_service = input("Enter the service name: ")

# Construct the API request
url = f"{api_endpoint}/{input_service}"

# Send the request and get the response
response = requests.get(url)

# Check if the response was successful
if response.status_code == 200:
    # Parse the JSON response
    response_json = response.json()

    # Check if the service has reached its end of life
    if isinstance(response_json, list):
        for version in response_json:
            if version.get("eol") is not None:
                print(f"The service {input_service} version {version.get('cycle')} has reached its end of life on {version.get('eol')}.")
            else:
                print(f"The service {input_service} version {version.get('cycle')} has not reached its end of life.")
    else:
        if response_json.get("eol") is None:
            print(f"The service {input_service} has not reached its end of life.")
        else:
            print(f"The service {input_service} has reached its end of life on {response_json['eol']}.")
else:
    print(f"Failed to retrieve information about the service {input_service}.")
