import shutil
import datetime
import os

class BackupSystem:
    @staticmethod
    def create_backup():
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
        backup_dir = f"storage/shared/tiktok-bot/backups/{timestamp}"
        
        os.makedirs(backup_dir, exist_ok=True)
        shutil.copy2("database/accounts.db", f"{backup_dir}/accounts.db")
        shutil.copy2(".env", f"{backup_dir}/env.bak")
        
        return backup_dir
    
    @staticmethod
    def restore_backup(timestamp):
        backup_dir = f"storage/shared/tiktok-bot/backups/{timestamp}"
        shutil.copy2(f"{backup_dir}/accounts.db", "database/accounts.db")
        shutil.copy2(f"{backup_dir}/env.bak", ".env")