from selenium.webdriver.common.by import By
from utilities.gmail_api import GmailService
from utilities.database_handler import AccountDB
import time
import random

class AccountCreator:
    def __init__(self, driver):
        self.driver = driver
        self.db = AccountDB()
        self.gmail = GmailService(
            os.getenv("GMAIL_USER"), 
            os.getenv("GMAIL_APP_PASSWORD")
        )
    
    def create_tiktok_account(self):
        email, hashed_pw, salt = self.db.get_account()
        
        # Paso 1: Registro en TikTok
        self.driver.get("https://www.tiktok.com/signup")
        time.sleep(3)
        
        # Seleccionar registro con email
        self.driver.find_element(By.XPATH, '//div[contains(text(), "Use email")]').click()
        time.sleep(1)
        
        # Ingresar datos
        self._fill_field("email", email)
        self._fill_field("password", self._decrypt_password(hashed_pw, salt))
        
        # Paso 2: Verificación
        verification_code = self.gmail.get_verification_code()
        self._fill_field("verificationCode", verification_code)
        
        # Actualizar base de datos
        self.db.update_usage(email)
    
    def _fill_field(self, name, value):
        field = self.driver.find_element(By.NAME, name)
        field.send_keys(value)
        time.sleep(random.uniform(0.5, 1.2))
    
    def _decrypt_password(self, hashed_pw, salt):
        # Implementar lógica de desencriptación según tu método
        return "tu_contraseña_descifrada"