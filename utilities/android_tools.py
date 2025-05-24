import os
from termux import storage

class AndroidStorageManager:
    @staticmethod
    def save_logs():
        storage_path = storage.get_external_storage_path()
        os.system(f"cp bot.log {storage_path}/tiktok-bot/logs/")
    
    @staticmethod
    def cleanup():
        os.system("rm -rf /data/data/com.termux/files/usr/tmp/*")