import json
from email_verifier import EmailVerifier
from captcha_solver import CaptchaSolver
from selenium.webdriver.common.by import By

class AccountGenerator:
    def __init__(self):
        self.verifier = EmailVerifier()
        self.captcha = CaptchaSolver()
    
    def create_account(self, driver, referral_code=None):
        driver.get("https://www.tiktok.com/signup")
        time.sleep(3)
        
        # Generar email temporal
        temp_email = self.verifier.get_temp_email()
        
        # Rellenar formulario
        driver.find_element(By.NAME, "email").send_keys(temp_email)
        if referral_code:
            driver.find_element(By.NAME, "referralCode").send_keys(referral_code)
        
        # Resolver CAPTCHA
        self.captcha.solve_and_input(driver)
        
        # Verificar email
        verification_code = self.verifier.fetch_verification_code(temp_email)
        driver.find_element(By.NAME, "verificationCode").send_keys(verification_code)
        
        return {
            "email": temp_email,
            "status": "created",
            "verification_code": verification_code
        }