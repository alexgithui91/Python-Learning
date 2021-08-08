def print_two(*args):
    arg1, arg2 = args
    print("arg1: %s arg2: %s" % (arg1, arg2))


def print_two_again(arg1, arg2):
    print("arg1: %s arg2: %s" % (arg1, arg2))


def print_one(arg1):
    print("arg1: %s " % arg1)


def print_none():
    print("Prints nothing")


print_two("Alex", "Githui")
print_two_again("Diana", "Kiragu")
print_one("Soi")
print_none()
