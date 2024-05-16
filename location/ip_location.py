import requests

def get_ip_location(ip_address):
    try:
        # Send a request to the ipinfo.io API with the provided IP address
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        # Raise an error if the request was unsuccessful
        response.raise_for_status()
        # Parse the JSON response
        data = response.json()

        # Extract relevant information
        location_info = {
            "IP": data.get("ip"),
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country"),
            "Location": data.get("loc"),  # Latitude and Longitude
            "Organization": data.get("org"),
            "Postal": data.get("postal"),
            "Timezone": data.get("timezone")
        }

        return location_info

    except requests.RequestException as e:
        print(f"Error fetching data for IP {ip_address}: {e}")
        return None

if __name__ == "__main__":
    # Prompt the user to enter an IP address
    ip_address = input("Enter the IP address: ")
    # Get the location information for the entered IP address
    location = get_ip_location(ip_address)
    
    # If location information is available, print it
    if location:
        print("\nLocation information:")
        for key, value in location.items():
            print(f"{key}: {value}")
