from social_media_bot import SocialMediaBot
from selenium.webdriver.common.by import By
import random

class YouTubeShortsBot(SocialMediaBot):
    def watch_video(self):
        self.driver.get("https://www.youtube.com/shorts")
        self._simulate_human_swipe()
    
    def _simulate_human_swipe(self):
        body = self.driver.find_element(By.TAG_NAME, 'body')
        for _ in range(3):
            body.send_keys(Keys.ARROW_DOWN)
            time.sleep(random.uniform(1.5, 2.8))
    
    def interact(self):
        self.like_video()
        self.post_comment("¡Increíble Short! 🚀")
    
    def get_platform_name(self):
        return "YouTube Shorts"