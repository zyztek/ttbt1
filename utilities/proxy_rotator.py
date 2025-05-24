import requests
from bs4 import BeautifulSoup
import random

class ProxyManager:
    PROXY_SOURCES = [
        "https://free-proxy-list.net",
        "https://www.sslproxies.org"
    ]
    
    def __init__(self):
        self.proxies = self._fetch_proxies()
    
    def _fetch_proxies(self):
        proxies = []
        for url in self.PROXY_SOURCES:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            for row in soup.select("table tbody tr"):
                cols = row.find_all("td")
                if len(cols) >= 2:
                    ip = cols[0].text.strip()
                    port = cols[1].text.strip()
                    proxies.append(f"{ip}:{port}")
        return proxies
    
    def get_proxy(self):
        return random.choice(self.proxies)