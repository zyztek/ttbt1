from selenium.webdriver import ChromeOptions
from fake_useragent import UserAgent
import random

class FingerprintManager:
    @staticmethod
    def get_random_fingerprint():
        ua = UserAgent()
        resolutions = ["1920x1080", "1366x768", "1440x900"]
        
        return {
            "user_agent": ua.random,
            "resolution": random.choice(resolutions),
            "platform": random.choice(["Win32", "Linux x86_64"]),
            "webgl_hash": f"#{random.randint(1000, 9999):04x}"  # Hash falso
        }
    
    @staticmethod
    def apply_fingerprint(options: ChromeOptions):
        fp = FingerprintManager.get_random_fingerprint()
        options.add_argument(f"--user-agent={fp['user_agent']}")
        options.add_argument(f"--window-size={fp['resolution'].split('x')[0]},{fp['resolution'].split('x')[1]}")
        return options