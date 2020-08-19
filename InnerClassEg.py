class Student:
    def __init__(self, name, rNo):
        self.name = name
        self.rNo = rNo
        # Creating object of Inner Class Laptop
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rNo)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.CPU = "i5"
            self.RAM = 12

        def show(self):
            print(self.brand, self.CPU, self.RAM)


s1 = Student('Roja', 35)
s2 = Student('Navin', 2)

s1.show()
s2.show()

# Creating object outside Outer Class
# Calling by Student cz its belongs to Student cls
lap1 = Student.Laptop()

# This is one way to call
# s1.lap.brand

lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))
