'''
Author : Alex Githui
Purpose : Read email using G-Mail
Created : 2021-04-07
'''

import imaplib
import os
import email
from dotenv import load_dotenv
load_dotenv()


host = os.environ.get('hostRead')
username = os.environ.get('emailUsername')
password = os.environ.get('emailPassword')


def getInbox():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username,password)
    mail.select("inbox")
    _, searchData = mail.search(None, 'UNSEEN')
    myMessage = []

    for num in searchData[0].split():
        emailData = {}
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        emailMessage = email.message_from_bytes(b)

        for header in ['subject', 'to', 'from', 'date']:
            print("{}: {}".format(header,emailMessage[header]))
            emailData[header] = emailMessage[header]

        for part in emailMessage.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                emailData['body'] = body.decode()
            elif part.get_content_type == "text/html":
                htmlBody = part.get_payload(decode=True)
                emailData['htmlBody'] = htmlBody.decode()

        myMessage.append(emailData)
    
    return myMessage

if __name__ == "__main__":
    myInbox = getInbox()
    print(myInbox)