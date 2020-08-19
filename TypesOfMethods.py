class Student:
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m2) / 3

    def get_m1(self):
        print("From get_m1")
        return self.m1

    def set_m1(self, value):
        print("From set_m1")
        self.m1 = value


s1 = Student(34, 49, 39)
s2 = Student(89, 88, 85)

print(s1.avg())
print(s2.avg())

print(s1.get_m1())
print(s1.set_m1(s1), 25)

print("Accessing single value ", s1.m1)
