import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    subject = 'Grab dinner'
    body = 'Good one'
    
    msg = f'Subject: {subject}\n\n{body}'
    
    smtp.sendmail(EMAIL_ADDRESS, 'mohamedabdifatah028@gmail.com', msg)