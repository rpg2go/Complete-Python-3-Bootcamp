import requests
import csv
import logging
from typing import List, Dict

# Set up logging for better error tracking
logging.basicConfig(level=logging.INFO)

class ApiDataProcessor:
    def __init__(self, api_url: str, csv_filename: str):
        self.api_url = api_url
        self.csv_filename = csv_filename

    def fetch_data(self) -> List[Dict]:
        """Fetch data from API and return it as a list of dictionaries."""
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # This automatically raises an HTTPError for 4xx/5xx responses
            return response.json()  # Returns the response in JSON format
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data: {e}")
            return []

    def save_to_csv(self, data: List[Dict]) -> None:
        """Save the fetched data into a CSV file."""
        if not data:
            logging.warning("No data to save.")
            return
        
        try:
            keys = data[0].keys()
            with open(self.csv_filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
            logging.info(f"Data successfully saved to {self.csv_filename}")
        except Exception as e:
            logging.error(f"Error saving data to CSV: {e}")

    def process_data(self) -> None:
        """Fetch, process, and save data."""
        data = self.fetch_data()
        self.save_to_csv(data)

def main():
    api_url = "https://jsonplaceholder.typicode.com/posts"
    csv_filename = "data.csv"

    # Create an instance of ApiDataProcessor
    data_processor = ApiDataProcessor(api_url, csv_filename)

    # Process data: Fetch, save to CSV
    data_processor.process_data()

if __name__ == "__main__":
    main()