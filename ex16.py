from sys import argv

script, filename = argv
prompt = "?? "

print("We are going to erase %r" % filename)
print("If you DO NOT want that, hit CTRL-C (^C)")
print("If you WANT that, hit RETURN/ENTER")

input(prompt)

print("Opening file...")
target = open(filename, "w")

print("Truncating file...")
target.truncate()

print("Enter three lines:")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I will write these lines to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("As always remember to close it")
target.close()
