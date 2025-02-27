# main.py
import logging
from api_client import ApiClient
from csv_writer import CsvWriter
from data_processor import DataProcessor
from config import API_URL, CSV_FILENAME

def main():
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('app.log', mode='w')  # Log to file as well for long-term monitoring
        ]
    )

    # Initialize the components
    api_client = ApiClient(API_URL)
    csv_writer = CsvWriter(CSV_FILENAME)
    data_processor = DataProcessor(api_client, csv_writer)

    # Run the data processing
    data_processor.process_data()

if __name__ == "__main__":
    main()