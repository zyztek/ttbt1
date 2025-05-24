import imaplib
import email
from email.header import decode_header
import re

class GmailService:
    def __init__(self):
        self.imap = imaplib.IMAP4_SSL("imap.gmail.com")
        self.imap.login(
            os.getenv("MASTER_ACCOUNT"),
            os.getenv("APP_PASSWORD")
        )
    
    def get_verification_code(self):
        self.imap.select("INBOX")
        status, messages = self.imap.search(None, '(SUBJECT "TikTok Verification Code")')
        
        if status == "OK":
            latest_email_id = messages[0].split()[-1]
            _, msg_data = self.imap.fetch(latest_email_id, "(RFC822)")
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)
            
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode()
                        return self._extract_code(body)
            else:
                body = msg.get_payload(decode=True).decode()
                return self._extract_code(body)
        return None
    
    def _extract_code(self, text):
        match = re.search(r"\b\d{6}\b", text)
        return match.group() if match else None