import requests
from bs4 import BeautifulSoup
import random

class ProxyManager:
    SOURCES = [
        "https://free-proxy-list.net",
        "https://geonode.com/free-proxy-list"
    ]
    
    def __init__(self):
        self.proxies = self._fetch_proxies()
    
    def _fetch_proxies(self):
        proxies = []
        for url in self.SOURCES:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            for row in soup.select("table tbody tr"):
                cols = [td.text.strip() for td in row.find_all('td')]
                if len(cols) >= 2:
                    proxies.append(f"{cols[0]}:{cols[1]}")
        return list(set(proxies))
    
    def get_proxy(self):
        return random.choice(self.proxies)
    
    def rotate(self):
        self.proxies = self._fetch_proxies()