'''
Author : Alex Githui
Purpose : Send email using G-Mail
Created : 2021-03-31
'''

import smtplib
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
load_dotenv()

username = os.environ.get('emailUsername')
password = os.environ.get('emailPassword')
senderEmail = os.environ.get('emailAccount')
toEmails = os.environ.get('toEmails').split(",")
website = os.environ.get('websiteName')
host = os.environ.get('hostSend')
port = os.environ.get('port')
emailSubject = "Code Tester HitzCommitted Account Subscription"


def emailSender(emailSubject, emailBody, toEmails, html=None):
    assert isinstance(toEmails, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = senderEmail
    msg['To'] = " ".join(toEmails)
    msg['Subject'] = emailSubject

    txtPart = MIMEText(emailBody, 'plain')
    msg.attach(txtPart)

    if html is not None:
        # It will always take the HTML over the plain text
        # MIMEText("<h1> This is working...</h1>", 'html')
        htmlHeader = '<h3>' + html + '</h3>'
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


def messageFormatter(myName=None, myWebsite=None):
    msgTemplate = """Hello {name}, 
    <br>Thank you for joining the email chain for {website}. 
    <br>We are very happy to have you with us.
    """

    messageBody = msgTemplate.format(name=myName, website=myWebsite)

    return messageBody


def sendEmail(name, website=None, toEmails=None, verbose=False):
    assert toEmails is not None
    if website is not None:
        msg = messageFormatter(name, website)
    else:
        msg = messageFormatter(name)

    if verbose:
        print(name, website, toEmails)

    # Send message
    try:
        emailSender(emailSubject, msg, toEmails, html=msg)
        sent = True
    except BaseException:
        sent = False
    return sent


if __name__ == "__main__":
    name = "Alex"
    sendEmail(name, website=website, toEmails=toEmails, verbose=True)
