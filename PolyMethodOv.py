class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # Here we can use the method variable length
    # in which 2nd variable holds ** e.g. a**
    def sum(self, a=None, b=None, c=None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = a
        return s


s1 = Student(58, 69)
s2 = Student(69, 65)

print("Sum of 2 No.s : ", s1.sum(89, 21))
print("Sum of 3  No.s : ", s1.sum(89, 21, 5))
print("Num : ", s1.sum(895))
