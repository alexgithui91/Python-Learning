# Learning to work with classes

class Car():
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."


carOne = Car("Red", "20,000")

print(carOne)
