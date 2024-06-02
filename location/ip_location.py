import requests
import pandas as pd
import matplotlib.pyplot as plt

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

def display_data(location_info, column_widths):
    # Display the data in a table using pandas
    df = pd.DataFrame([location_info])
    print("\nLocation information:")
    print(df.to_string(index=False))

    # Plotting the data
    fig, ax = plt.subplots(figsize=(10, 4))  # Increase figure width for better readability
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
    
    # Adjust column widths and set color
    cell_dict = table.get_celld()
    for i, col in enumerate(df.columns):
        cell_dict[(0, i)].set_width(column_widths.get(col, 0.15))  # Column headers
        cell_dict[(1, i)].set_width(column_widths.get(col, 0.15))  # Data cells

    # Set color for the table headers
    for key, cell in cell_dict.items():
        cell.set_edgecolor('black')
        if key[0] == 0:  # Header row
            cell.set_facecolor('orange')
            cell.set_text_props(weight='bold', color='red')
        else:  # Data rows
            cell.set_facecolor('#f0f0f0')

    # Additional adjustments to font size of row and column labels if necessary
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    
    # Title
    plt.title('IP Details', fontsize=30, weight='bold', color='red')
    
    # Adjust space between title and table
    plt.subplots_adjust(top=0.85) 
    
    plt.show()

if __name__ == "__main__":
    # Prompt the user to enter an IP address
    ip_address = input("Enter the IP address: ")
    # Get the location information for the entered IP address
    location = get_ip_location(ip_address)
    
    # Column width settings
    column_widths = {
        "IP": 0.1,
        "City": 0.15,
        "Region": 0.15,
        "Country": 0.1,
        "Location": 0.20,  # Increase width for Location column
        "Organization": 0.30,
        "Postal": 0.1,
        "Timezone": 0.1
    }
    
    # If location information is available, print it and display it
    if location:
        display_data(location, column_widths)
