# Day 4

class Person():
    def __init__(self, initialAge):
        self.age = 0

        if initialAge > 0:
            self.age = initialAge
        else:
            print("Age is not valid, setting age to 0.")

    def amIOld(self):
        comment = None
        if age < 13:
            print("You are young.")
        elif age >= 13 and age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

        # return comment

    def yearPasses(self):
        # Increment the age of the person in here
        global age
        age += 1


t = int(input("Enter number of entries : "))

for i in range(0, t):
    age = int(input("Enter age : "))
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
