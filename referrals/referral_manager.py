import hashlib
from database_manager import DatabaseManager

class ReferralSystem:
    def __init__(self):
        self.db = DatabaseManager()
    
    def generate_referral_code(self, username):
        hash_object = hashlib.sha256(username.encode())
        return hash_object.hexdigest()[:8].upper()
    
    def track_conversion(self, code):
        self.db.conn.execute('''
            INSERT INTO referrals (code, conversion_date) 
            VALUES (?, CURRENT_TIMESTAMP)
        ''', (code,))
        self.db.conn.commit()
    
    def get_conversion_rate(self):
        result = self.db.conn.execute('''
            SELECT 
                COUNT(DISTINCT code) AS unique_codes,
                COUNT(*) AS total_conversions 
            FROM referrals
        ''').fetchone()
        return result['total_conversions'] / result['unique_codes'] if result['unique_codes'] > 0 else 0