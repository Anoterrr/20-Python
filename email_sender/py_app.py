# To test the aplication try visiting temp-mail.org

from email.message import EmailMessage
import ssl
import smtplib

em = EmailMessage()

email_sender = "Your email"
email_password = "Password genete by your email"
email_reciver = "Email that will recive"

subject = "Important topic"
body = """
Put something here to send 
"""

em['From'] = email_sender
em['To'] = email_reciver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTB_SSL('smtp.gmail.com', 456, context = context) as smtp: 
    smtp.login(email_sender, email_password)
    smtp.sendemail(email_sender, email_reciver, em.as_string())