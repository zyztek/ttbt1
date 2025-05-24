import requests
import re

class EmailVerifier:
    def get_temp_email(self):
        response = requests.get("https://api.tempmail.lol/generate")
        return response.json()['address']
    
    def fetch_verification_code(self, email):
        for _ in range(10):
            response = requests.get(f"https://api.tempmail.lol/inbox/{email}")
            if response.json():
                return re.search(r"\d{6}", response.json()[0]['body']).group()
            time.sleep(15)
        return None