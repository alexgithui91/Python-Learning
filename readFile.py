'''
Author : Alex Githui
Purpose : Read from a file
Created : 2021-04-07
'''

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

emailTxt = os.path.join(BASE_DIR, "templates", "email.txt")

content = ""

with open(emailTxt, 'r') as f:
    content = f.read()

print(content.format(name='TestUser'))
