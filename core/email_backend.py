import urllib.request
import json
from django.core.mail.backends.base import BaseEmailBackend
from django.conf import settings

class BrevoEmailBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        if not email_messages:
            return 0
            
        api_key = getattr(settings, 'BREVO_API_KEY', None)
        if not api_key:
            if not self.fail_silently:
                raise ValueError("BREVO_API_KEY is not configured in settings.")
            return 0
            
        sent_count = 0
        for message in email_messages:
            try:
                url = "https://api.brevo.com/v3/smtp/email"
                headers = {
                    "accept": "application/json",
                    "api-key": api_key,
                    "content-type": "application/json",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }
                
                sender_email = getattr(settings, 'BREVO_SENDER_EMAIL', 'mahalakshmisr725@gmail.com')
                
                # Format recipients for Brevo structure
                to_list = [{"email": email} for email in message.to]
                
                data = {
                    "sender": {
                        "name": "IdeaForge",
                        "email": sender_email
                    },
                    "to": to_list,
                    "subject": message.subject,
                    "htmlContent": message.body.replace("\n", "<br>")
                }
                
                req = urllib.request.Request(
                    url, 
                    data=json.dumps(data).encode('utf-8'), 
                    headers=headers, 
                    method='POST'
                )
                
                # Execute HTTP POST request
                with urllib.request.urlopen(req, timeout=10) as response:
                    if response.getcode() in [200, 201, 202]:
                        sent_count += 1
            except Exception as e:
                if not self.fail_silently:
                    raise e
                    
        return sent_count
