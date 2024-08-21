
import time
import random
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from rich.console import Console

console = Console()

def load_dorks(file_path):
    with open(file_path, 'r') as file:
        dorks = file.readlines()
    return [dork.strip() for dork in dorks]

def execute_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    response = requests.get(search_url)
    return response.text

def parse_results(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    results = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if "url?q=" in url:
            results.append(url.split("url?q=")[1].split("&")[0])
    return results

def main(dorks):
    for dork in dorks:
        console.log(f"Searching for: {dork}")
        html_content = execute_search(dork)
        results = parse_results(html_content)
        if results:
            console.log(f"Found {len(results)} results for dork: {dork}")
            # Save or process results here
        time.sleep(random.uniform(5, 10))  # Random delay between searches

if __name__ == "__main__":
    dork_list = load_dorks('data/dorks.txt')
    main(dork_list)
