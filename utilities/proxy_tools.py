import requests
from bs4 import BeautifulSoup
import random
import time

class ProxyEngine:
    SOURCES = [
        "https://free-proxy-list.net/anonymous-proxy.html",
        "https://www.sslproxies.org",
        "https://hidemy.name/es/proxy-list/"
    ]
    
    def __init__(self):
        self.proxies = []
        self.last_update = 0
        self._refresh_proxies()
    
    def _refresh_proxies(self):
        if time.time() - self.last_update < 3600:  # Actualizar cada 1 hora
            return
            
        new_proxies = []
        for url in self.SOURCES:
            try:
                response = requests.get(url, timeout=10)
                soup = BeautifulSoup(response.text, 'html.parser')
                rows = soup.select("table tbody tr")
                
                for row in rows:
                    cols = [td.text.strip() for td in row.find_all('td')]
                    if len(cols) >= 2 and cols[4] == "Elite Proxy":
                        new_proxies.append(f"{cols[0]}:{cols[1]}")
                
            except Exception as e:
                print(f"Error obteniendo proxies: {str(e)}")
        
        self.proxies = list(set(new_proxies))
        self.last_update = time.time()
    
    def get_proxy(self):
        self._refresh_proxies()
        return random.choice(self.proxies) if self.proxies else None
    
    def test_proxy(self, proxy):
        try:
            test_url = "https://api.ipify.org?format=json"
            response = requests.get(test_url, proxies={
                "http": f"http://{proxy}",
                "https": f"http://{proxy}"
            }, timeout=15)
            return response.status_code == 200
        except:
            return False