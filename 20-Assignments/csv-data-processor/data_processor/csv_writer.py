# csv_writer.py
import csv
import logging
from typing import List, Dict

class CsvWriter:
    def __init__(self, filename: str):
        self.filename = filename

    def save_to_csv(self, data: List[Dict]) -> None:
        """Saves the fetched data into a CSV file."""
        try:
            keys = data[0].keys()
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)
            logging.info(f"Data successfully saved to {self.filename}")
        except Exception as e:
            logging.error(f"Error saving data to CSV: {e}")