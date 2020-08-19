# a = '5'
# b = '6'

# print(a + b)
# print(str.__add__(a, b))


class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        print("s1 : ", m1)
        print("s2 : ", m2)
        s3 = Student(m1, m2)

        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(58, 56)
s2 = Student(85, 65)

# This another way of displaying values
# print(s1.__str__())

print("Values of S1 : ", s1)
print("Values of S2 : ", s2)

s3 = s1 + s2

if s1 < s2:
    print("S1 Wins")
else:
    print("S2 Wins")

print("S3 = S1 + S2 : ", s3.m1)
