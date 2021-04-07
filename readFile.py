'''
Author : Alex Githui
Purpose : Read from a file
Created : 2021-03-31
'''

import os

filePath = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(filePath)

emailTxt = os.path.join(BASE_DIR, "templates", "email.txt")

content = ""

with open(emailTxt, 'r') as f:
    content = f.read()

print(content.format(name='TestUser'))
