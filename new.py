import requests
from bs4 import BeautifulSoup
import time

def bing_search(query):
    base_url = "https://www.bing.com/search"
    params = {'q': query}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract and print the search results
        for result in soup.select('li.b_algo h2 a'):
            print(result.get('href'))

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Example usage
search_queries = ['pc', 'nbuhfehfa', 'cac', 'faaaaas', 'mm']

for query in search_queries:
    bing_search(query)
    time.sleep(0.4)  # Add a delay of 1 second between requests
