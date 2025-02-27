import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"
CSV_FILENAME = "data.csv"

# Fetch data from API
try:
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: Received status code {response.status_code}")
        data = []
except Exception as e:
    print(f"Error fetching data: {e}")
    data = []

# Save data to CSV
if len(data) > 0:
    try:
        keys = data[0].keys()
        file = open(CSV_FILENAME, "w", newline="", encoding="utf-8")
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
        file.close()
        print(f"Data saved to {CSV_FILENAME}")
    except Exception as e:
        print(f"Error saving data: {e}")
else:
    print("No data to save.")