# Learning how to work with classes

class Dog():
    # Class attributes
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old! And is {self.species}"

    # Another Instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


boscoe = Dog("Boscoe", 4)
print(boscoe)
# print(boscoe.description())
print(boscoe.speak("Woof Woooof"))