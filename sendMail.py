'''
Author : Alex Githui
Purpose : Send email using G-Mail
Created : 2021-03-31
'''

import smtplib
from email.mime.multipart import MIMEMultipart

username = 'codetestergithui@gmail.com'
password = 'codetester'
senderEmail = 'Code Tester Githui <codetestergithui@gmail.com>'
toEmails = ['alexgithui91@gmail.com']


def emailSender(
        text='Email Body',
        subject='Hello World',
        fromEmail=senderEmail,
        toEmails=toEmails):
    assert isinstance(toEmails, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = senderEmail
    msg['To'] = ", ".join(toEmails)
    msg['Subject'] = subject

    txtPart = MIMEMultipart(text, 'plain')
    msg.attach(txtPart)

    htmlPart = MIMEMultipart("<h1> This is working...</h1>", 'html')
    msg.attach(htmlPart)

    msgStr = msg.as_string()

    # Login to the smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromEmail, toEmails, msgStr)
    server.quit()


emailSender()
