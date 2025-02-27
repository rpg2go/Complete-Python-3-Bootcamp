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

# Example JSON data
# [
#     {"name": "John", "age": 30, "createdDateTime": "2025-01-02 23:10:03"},
#     {"name": "Jane", "age": 25, "createdDateTime": "2025-01-02 24:10:03"},  # Invalid timestamp
#     {"name": "Doe", "age": 22, "createdDateTime": "2025-01-02 23:67:03"}    # Invalid timestamp
# ]

# Save data to CSV
if len(data) > 0:
    try:
        keys = data[0].keys()
        file = open(CSV_FILENAME, "w", newline="", encoding="utf-8")
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()

        ## as it 
        writer.writerows(data)

        ## TODO: Iterate through the json data, validate the createdDateTime attribute for each 
        ##  ....replace with actual code....

        file.close()
        print(f"Data saved to {CSV_FILENAME}")
    except Exception as e:
        print(f"Error saving data: {e}")
else:
    print("No data to save.")