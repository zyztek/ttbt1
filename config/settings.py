import os
import json
from dotenv import load_dotenv

load_dotenv()

class Config:
    @staticmethod
    def get(key, default=None):
        return os.getenv(key, default)
    
    @staticmethod
    def load_json_config():
        with open('config/settings.json') as f:
            return json.load(f)
    
    @staticmethod
    def get_limits():
        return {
            "views_per_hour": int(Config.get("MAX_VIEWS_PER_HOUR", 50)),
            "max_accounts": int(Config.get("MAX_ACCOUNTS", 3)),
            "proxy_rotation": int(Config.get("PROXY_ROTATION_MINUTES", 15))
        }