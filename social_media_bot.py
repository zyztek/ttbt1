from abc import ABC, abstractmethod
from selenium.webdriver import Chrome

class SocialMediaBot(ABC):
    def __init__(self, driver: Chrome):
        self.driver = driver
    
    @abstractmethod
    def watch_video(self):
        pass
    
    @abstractmethod
    def like_content(self):
        pass
    
    @abstractmethod
    def get_platform_name(self):
        pass

class TikTokBot(SocialMediaBot):
    def watch_video(self):
        # Implementación específica de TikTok
        self.driver.find_element(...)
    
    def like_content(self):
        # Lógica de likes para TikTok
        pass
    
    def get_platform_name(self):
        return "TikTok"

class InstagramReelsBot(SocialMediaBot):
    def watch_video(self):
        # Implementación para Reels
        self.driver.get("https://instagram.com/reels")
        pass