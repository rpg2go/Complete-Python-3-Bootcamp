# data_processor.py
import logging
from api_client import ApiClient
from csv_writer import CsvWriter
from config import API_URL, CSV_FILENAME

class DataProcessor:
    def __init__(self, api_client: ApiClient, csv_writer: CsvWriter):
        self.api_client = api_client
        self.csv_writer = csv_writer

    def process_data(self) -> None:
        """Orchestrates fetching, processing, and saving data."""
        logging.info("Starting data processing...")
        data = self.api_client.fetch_data()
        if data:
            self.csv_writer.save_to_csv(data)
        else:
            logging.warning("No data available to process.")