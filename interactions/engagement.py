from selenium.webdriver.common.keys import Keys
from database_manager import DatabaseManager

class EngagementManager:
    def __init__(self, driver):
        self.driver = driver
        self.db = DatabaseManager()
    
    def like_video(self):
        try:
            like_btn = self.driver.find_element(By.XPATH, '//div[@data-e2e="like-icon"]')
            like_btn.click()
            self.db.log_action("LIKE", {"status": "success"})
            return True
        except Exception as e:
            self.db.log_action("LIKE", {"status": "failed", "error": str(e)})
            return False
    
    def share_video(self, method="link"):
        try:
            self.driver.find_element(By.XPATH, '//div[@data-e2e="share-icon"]').click()
            time.sleep(1)
            
            if method == "link":
                self.driver.find_element(By.XPATH, '//div[contains(text(), "Copiar enlace")]').click()
            elif method == "dm":
                self._send_direct_message()
            
            self.db.log_action("SHARE", {"method": method})
            return True
        except Exception as e:
            self.db.log_action("SHARE", {"status": "failed", "error": str(e)})
            return False