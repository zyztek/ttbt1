import os
import requests
from selenium.webdriver.common.by import By
from .captcha_solver import solve_captcha
from .proxy_manager import ProxyManager

class AuthManager:
    def __init__(self, driver, db):
        self.driver = driver
        self.db = db
        self.proxy_manager = ProxyManager(db)

    def authenticate_zefoy(self):
        """Autentica en Zefoy resolviendo CAPTCHAs y guardando cookies."""
        self.driver.get("https://zefoy.com")
        time.sleep(5)
        
        # Resolver CAPTCHA
        captcha_image = self.driver.find_element(By.XPATH, '//img[@alt="CAPTCHA"]')
        captcha_image.screenshot("captcha.png")
        captcha_text = solve_captcha("captcha.png")
        
        # Enviar solución
        input_field = self.driver.find_element(By.NAME, 'captcha')
        input_field.send_keys(captcha_text)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        
        # Guardar cookies en DB
        cookies = self.driver.get_cookies()
        self.db.update_service_auth('zefoy', {'cookies': cookies})

    def authenticate_tiktok_api(self):
        """Obtiene token de API de TikTok via Selenium."""
        self.driver.get("https://www.tiktok.com/login")
        time.sleep(10)
        
        # Esperar login manual y extraer token (alternativa automática)
        token = self.driver.execute_script('return window.localStorage.getItem("auth_token");')
        self.db.update_service_auth('tiktok', {'token': token})