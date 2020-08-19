class Car:
    wheels = 4  # Class Variable

    def __init__(self):
        self.mil = 10  # Instance Variable
        self.com = "BMW"


c1 = Car()
c2 = Car()  

c1.mil = 8  # Instance Variable

# Class Variable : changing the value will affect to entire pgm
Car.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
