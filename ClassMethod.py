class Student:
    school = "Tele"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m2) / 3

    @classmethod
    def getSchool(cls):
        print("This is Class method")
        return cls.school

    @staticmethod
    def info():
        print("This is Static Method")


s1 = Student(34, 49, 39)
s2 = Student(89, 88, 85)

print(s1.avg())
print(s2.avg())

print(Student.getSchool())
Student.info()
