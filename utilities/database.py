import sqlite3
from cryptography.fernet import Fernet
import os

class AccountManager:
    def __init__(self):
        self.conn = sqlite3.connect(os.path.expanduser('~/storage/shared/tiktok-bot/db/accounts.db'))
        self.cipher = Fernet(os.getenv("ENCRYPTION_KEY"))
        self._init_db()
    
    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY,
                email TEXT UNIQUE,
                encrypted_password TEXT,
                last_used REAL,
                success_rate REAL DEFAULT 1.0
            )
        ''')
        self.conn.commit()
    
    def add_account(self, email, password):
        encrypted = self.cipher.encrypt(password.encode())
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO accounts (email, encrypted_password)
            VALUES (?, ?)
        ''', (email, encrypted))
        self.conn.commit()
    
    def get_next_account(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT email, encrypted_password 
            FROM accounts 
            ORDER BY last_used ASC 
            LIMIT 1
        ''')
        row = cursor.fetchone()
        return {
            'email': row[0],
            'password': self.cipher.decrypt(row[1]).decode()
        }