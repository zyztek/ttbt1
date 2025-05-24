import logging
from selenium.common.exceptions import WebDriverException

class ErrorManager:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
    
    def handle_possible_ban(self):
        """Reacciona ante posibles baneos detectados"""
        if "captcha" in self.driver.page_source.lower():
            self.logger.warning("CAPTCHA detectado - Iniciando protocolo de limpieza")
            self._clean_session()
            return True
        return False
    
    def _clean_session(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script("window.localStorage.clear()")
        self.driver.refresh()
    
    def retry_operation(self, func, max_retries=3):
        """Intento inteligente de operaciones fallidas"""
        for attempt in range(max_retries):
            try:
                return func()
            except WebDriverException as e:
                self.logger.error(f"Intento {attempt+1} fallido: {str(e)}")
                self._rotate_proxy()
        raise Exception("Operación fallida después de múltiples intentos")