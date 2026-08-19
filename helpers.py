import time
import requests
from requests.exceptions import RequestException


def retry_request(url, max_retries=3, backoff_factor=1):
    """
    Perform a network request with retry logic.
    
    :param url: The URL to send the request to.
    :param max_retries: Maximum number of retries.
    :param backoff_factor: Backoff factor for sleep time.
    :return: Response object if successful, None otherwise.
    """
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except RequestException as e:
            retries += 1
            wait_time = backoff_factor * (2 ** (retries - 1))
            print(f"Attempt {retries} failed: {e}. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
    print(f"All {max_retries} attempts failed.")
    return None