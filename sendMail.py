'''
Author : Alex Githui
Purpose : Send email using G-Mail
Created : 2021-03-31
'''

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
load_dotenv()

username = os.environ.get('emailUsername')
password = os.environ.get('emailPassword')
senderEmail = os.environ.get('emailAccount')
toEmails = os.environ.get('toEmails').split(",")
host = os.environ.get('host')
port = os.environ.get('port')


def emailSender(emailSubject, emailBody, toEmails, html=None):
    assert isinstance(toEmails, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = senderEmail
    msg['To'] = "".join(toEmails)
    msg['Subject'] = emailSubject

    txtPart = MIMEText(emailBody, 'plain')
    msg.attach(txtPart)

    if html is not None:
        # It will always take the HTML over the plain text
        # MIMEText("<h1> This is working...</h1>", 'html')
        htmlHeader = '<h1>' + html + '</h1>'
        htmlPart = MIMEText(htmlHeader, 'html')
        msg.attach(htmlPart)

    msgStr = msg.as_string()

    # Login to the smtp server
    server = smtplib.SMTP(host=host, port=port)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(senderEmail, toEmails, msgStr)
    server.quit()


def messageFormatter(myName, myWebsite):
    msgTemplate = """ Hello {name},
    Thank you for joining the email chain for {website}.
    We are very happy to have you with us.
    """

    messageBody = msgTemplate.format(name=myName, website=myWebsite)

    return messageBody


# Ask for email subject
emailSubject = input("Enter email subject : ")
# Ask for email body/contents
emailBody = input("Enter email body : ")
# Enter HTML contents
html = input("Enter HTML contents : ")

emailSender(emailSubject, emailBody, toEmails, html)
