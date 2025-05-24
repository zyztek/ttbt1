import imaplib
import email
import re
from email.header import decode_header

class GmailVerifier:
    def __init__(self):
        self.imap = imaplib.IMAP4_SSL("imap.gmail.com")
        self._authenticate()
    
    def _authenticate(self):
        self.imap.login(
            os.getenv("GMAIL_MASTER"),
            os.getenv("GMAIL_APP_PASSWORD")
        )
    
    def get_tiktok_code(self):
        self.imap.select("INBOX")
        status, messages = self.imap.search(None, '(SUBJECT "TikTok Verification Code")')
        
        if status != "OK":
            return None

        for msg_num in messages[0].split()[-3:]:  # Últimos 3 emails
            _, msg_data = self.imap.fetch(msg_num, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])
            code = self._extract_code(msg)
            if code:
                return code
        return None
    
    def _extract_code(self, msg):
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    return re.search(r"\d{6}", body).group()
        return None