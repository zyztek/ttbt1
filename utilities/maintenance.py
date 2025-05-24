import sqlite3
import os

class DBOptimizer:
    def __init__(self):
        self.db_path = "storage/shared/tiktok-bot/db/accounts.db"
    
    def vacuum_database(self):
        """Optimiza el espacio de la base de datos"""
        conn = sqlite3.connect(self.db_path)
        conn.execute("VACUUM")
        conn.close()
    
    def clean_old_logs(self, days=7):
        """Elimina logs antiguos"""
        log_dir = "storage/shared/tiktok-bot/logs/"
        cutoff = time.time() - (days * 86400)
        
        for f in os.listdir(log_dir):
            file_path = os.path.join(log_dir, f)
            if os.stat(file_path).st_mtime < cutoff:
                os.remove(file_path)