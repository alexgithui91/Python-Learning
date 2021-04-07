'''
Author : Alex Githui
Purpose : Send email using G-Mail
Created : 2021-04-07
'''

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filesDir = os.path.join(BASE_DIR, "templates")

os.makedirs(filesDir, exist_ok=True)

myFiles = range(0, 12)

for i in myFiles:
    fileName = f"{i}.txt"
    filePath = os.path.join(filesDir, fileName)
    if os.path.exists(filePath):
        print(f"Skipped {fileName} Already exists")
        continue

    with open(filePath, 'w') as f:
        f.write(i * "Hey hey hey!!!\n")
