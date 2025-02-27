# api_client.py
import requests
import logging
from time import sleep
from requests.exceptions import RequestException
from typing import Optional, List, Dict
from config import API_URL, MAX_RETRIES, BACKOFF_FACTOR

class ApiClient:
    def __init__(self, api_url: str = API_URL, max_retries: int = MAX_RETRIES, backoff_factor: float = BACKOFF_FACTOR):
        self.api_url = api_url
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def fetch_data(self) -> Optional[List[Dict]]:
        """Fetch data from the API with retry logic and exponential backoff."""
        retries = 0
        while retries <= self.max_retries:
            try:
                response = requests.get(self.api_url)
                response.raise_for_status()  # Automatically raises for 4xx and 5xx status codes
                return response.json()  # Returns the response as JSON
            except RequestException as e:
                logging.error(f"Error fetching data from API: {e}. Retrying...")
                retries += 1
                if retries > self.max_retries:
                    logging.critical("Maximum retry attempts reached. Failed to fetch data.")
                    return None
                sleep(self.backoff_factor * (2 ** retries))  # Exponential backoff
        return None