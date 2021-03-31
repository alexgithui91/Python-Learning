'''
Author : Alex Githui
Purpose : Send email using G-Mail
Created : 2021-03-31
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'codetestergithui@gmail.com'
password = 'codetester'
senderEmail = 'Code Tester Githui <codetestergithui@gmail.com>'


def emailSender(emailSubject, emailBody, toEmails, html=None):
    assert isinstance(toEmails, list)

    msg = MIMEMultipart('alternative')
    msg['From'] = senderEmail
    msg['To'] = ", ".join(toEmails)
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
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(senderEmail, toEmails, msgStr)
    server.quit()


# Ask for email subject
emailSubject = input("Enter email subject : ")
# Ask for email body/contents
emailBody = input("Enter email body : ")
# Enter HTML contents
html = input("Enter HTML contents : ")
# Enter email addresses
toEmails = ['alexgithui91@gmail.com']

emailSender(emailSubject, emailBody, toEmails, html)
