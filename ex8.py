formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(
    formatter %
    ("This is test statement 1",
     "This is test statement 2",
     "This is test statement 3",
     "This is test statement 4"))
