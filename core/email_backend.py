import urllib.request
import json
from django.core.mail.backends.base import BaseEmailBackend
from django.conf import settings

class ResendEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        if not email_messages:
            return 0
            
        api_key = getattr(settings, 'RESEND_API_KEY', None)
        if not api_key:
            if not self.fail_silently:
                raise ValueError("RESEND_API_KEY is not configured in settings.")
            return 0
            
        sent_count = 0
        for message in email_messages:
            try:
                url = "https://api.resend.com/emails"
                headers = {
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }
                
                from_email = getattr(settings, 'RESEND_FROM_EMAIL', 'onboarding@resend.dev')
                
                # Resend accepts a single string or a list of emails for "to"
                to_emails = list(message.to)
                
                data = {
                    "from": from_email,
                    "to": to_emails,
                    "subject": message.subject,
                    "text": message.body,
                    "html": message.body.replace("\n", "<br>")
                }
                
                req = urllib.request.Request(
                    url, 
                    data=json.dumps(data).encode('utf-8'), 
                    headers=headers, 
                    method='POST'
                )
                
                # Execute HTTP POST request
                with urllib.request.urlopen(req, timeout=10) as response:
                    if response.getcode() in [200, 201]:
                        sent_count += 1
            except Exception as e:
                if not self.fail_silently:
                    raise e
                    
        return sent_count
