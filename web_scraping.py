import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, user_agent='aiDorkBot'):
        self.headers = {'User-Agent': user_agent}

    def get_html(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching URL {url}: {e}")
            return None

    def extract_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return [a['href'] for a in soup.find_all('a', href=True)]
