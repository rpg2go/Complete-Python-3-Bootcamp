import requests
import csv
import logging
from typing import List, Dict, Optional
from requests.exceptions import RequestException
from time import sleep

# Set up logging with a more advanced configuration (including timestamps)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('app.log', mode='w')  # Log to file as well for long-term monitoring
    ]
)

class ApiDataProcessor:
    def __init__(self, api_url: str, csv_filename: str, max_retries: int = 3, backoff_factor: float = 1.0):
        """
        Initializes the ApiDataProcessor with API URL, CSV file name, retry configuration.
        
        :param api_url: The URL for the API request
        :param csv_filename: The name of the CSV file to save data to
        :param max_retries: The maximum number of retries for failed API requests
        :param backoff_factor: The backoff factor for exponential retry delay
        """
        self.api_url = api_url
        self.csv_filename = csv_filename
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def _get_api_data(self) -> Optional[List[Dict]]:
        """
        Attempts to fetch data from the API with retry logic and exponential backoff.

        :return: A list of dictionaries containing the data or None if the fetch fails after retries
        """
        retries = 0
        while retries <= self.max_retries:
            try:
                response = requests.get(self.api_url)
                response.raise_for_status()  # This raises an exception for 4xx and 5xx status codes
                return response.json()  # Assumes the response is JSON
            except RequestException as e:
                logging.error(f"Error fetching data from API: {e}. Retrying...")
                retries += 1
                if retries > self.max_retries:
                    logging.critical("Maximum retry attempts reached. Failed to fetch data.")
                    return None
                sleep(self.backoff_factor * (2 ** retries))  # Exponential backoff
        return None

    def _save_to_csv(self, data: List[Dict]) -> None:
        """
        Saves data to a CSV file.
        
        :param data: The data to be saved in CSV format
        """
        try:
            keys = data[0].keys()
            with open(self.csv_filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
            logging.info(f"Data successfully saved to {self.csv_filename}")
        except Exception as e:
            logging.error(f"Error saving data to CSV: {e}")

    def process_data(self) -> None:
        """
        Fetches data from the API, processes it, and saves it to a CSV file.
        """
        logging.info("Starting data processing...")
        data = self._get_api_data()
        if data:
            self._save_to_csv(data)
        else:
            logging.warning("No data available to process.")

class DataProcessorManager:
    def __init__(self, api_url: str, csv_filename: str):
        """
        Manages the lifecycle of the ApiDataProcessor and handles the orchestration.
        
        :param api_url: The URL for the API request
        :param csv_filename: The name of the CSV file to save data to
        """
        self.data_processor = ApiDataProcessor(api_url, csv_filename)

    def run(self) -> None:
        """Runs the data processing pipeline."""
        self.data_processor.process_data()

def main():
    api_url = "https://jsonplaceholder.typicode.com/posts"
    csv_filename = "data.csv"
    
    # Create the DataProcessorManager to manage the process
    manager = DataProcessorManager(api_url, csv_filename)

    # Run the process
    manager.run()

if __name__ == "__main__":
    main()