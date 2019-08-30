import os
from st2common.runners.base_action import Action
from smtplib import SMTP
from email.header import Header

class SendEmail(Action):
    def run(self, email_from, email_to, subject, messag)
        s = SMTP(account_data['server'], int(account_data['port']), timeout=20)
        s.ehlo()
        if account_data.get('secure', True) is True:
            s.starttls()
        if account_data.get('smtp_auth', True) is True:
            s.login(account_data['username'], account_data['password'])
        s.sendmail(email_from, email_to, msg.as_string())
        s.quit()
        return
