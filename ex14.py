from sys import argv

script, user_name = argv
prompt = "> "

print("Hi %s! I am the %s script." % (user_name, script))
print("I will ask you a few questions")
print("%s have you ever heard of me?" % user_name)
know_me = input(prompt)

print("Where are you located %s?" % user_name)
location = input(prompt)

print("%s what kinda computer you got?" % user_name)
computer = input(prompt)

print(
    """
Alright then! Just to confirm, you are %s.
You are located in %s and your computer is a %s"""
    % (user_name, location, computer)
)
