import requests
import os

def fetch_nhl_data(url, fileName):

    if os.path.exists(fileName):
        print(f"skip fetch: {fileName}")
        return

    response = requests.get(url)

    if response.status_code == 200:
        csv_data = response.text
    
        with open(fileName, 'w', newline='') as f:
            f.write(csv_data)
        
        print(f"Data has been fetched and written to {fileName}")
    else:
        print("Failed to fetch data. Status code:", response.status_code)