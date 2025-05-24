import time
import random
from selenium.webdriver.common.by import By
from utilities.gmail_client import GmailVerifier

class AccountCreator:
    def __init__(self, driver):
        self.driver = driver
        self.verifier = GmailVerifier()
    
    def create_account(self, email, password):
        try:
            self.driver.get("https://www.tiktok.com/signup")
            time.sleep(random.uniform(3, 5))
            
            # Seleccionar registro por email
            self.driver.find_element(By.XPATH, '//div[text()="Use email"]').click()
            time.sleep(1)
            
            # Ingresar datos
            self._fill_field("email", email)
            self._fill_field("password", password)
            
            # Verificar código
            code = self.verifier.get_tiktok_code()
            if code:
                self._fill_field("verificationCode", code)
                time.sleep(5)
                return True
            return False
            
        except Exception as e:
            print(f"Error creando cuenta: {str(e)}")
            return False
    
    def _fill_field(self, name, value):
        field = self.driver.find_element(By.NAME, name)
        field.clear()
        for char in value:
            field.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))