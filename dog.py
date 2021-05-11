# Practicing Classes in Python

class Dog():
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old!"

    def speak(self, sound):
        return f"{self.name} barks barks {sound}"

class GoldenRetriever(Dog):
    def speak(self, sound="WOOF WOOF"):
        # return f"{self.name} says {sound}"
        return super().speak("hooooooowl")

rexxie = GoldenRetriever("Brian", 4)

print(rexxie.speak())