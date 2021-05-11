# Learning how to work with classes

class Dog():
    # Class attributes
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
        # self.breed = breed

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old! And is species {self.species}"

    # Another Instance method
    def speak(self, sound):
        return f"{self.name} barks : {sound}!!!"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        # return f"{self.name} says {sound}"
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

boscoe = JackRussellTerrier("Boscoe", 3)
print(boscoe)
print(boscoe.speak())
# rex = Bulldog("Rex", 4)
# print(rex)
# print(rex.speak("hey"))