from sys import argv
from os.path import exists

script, from_file = argv

print("Would you like to copy %s?" % from_file)
to_file = input("Enter new file name : ")
response = input("Copy %s to %s? y/n ")

if response == "y":
    indata = open(from_file).read()
    if exists(to_file):
        print("File exists.")
    else:
        out_file = open(to_file, "w")
        out_file.write(indata)
        print("File copied.")
elif response == "n":
    print("File not copied.")
else:
    print("Bad response. Quiting.")
