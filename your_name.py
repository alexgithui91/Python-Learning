name = input("Enter your name: ")

checkName = ''

while checkName != name:
    checkName = input("Please type your name again: ")

print("Thank you!")

'''
originalName = input("Enter name: ")

while True:
    name = input("Please re-enter your name: ")
    if name == originalName:
        break

print("Thank You!")
'''
