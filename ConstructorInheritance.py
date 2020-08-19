class A:
    def __init__(self):
        print("Init of A")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B:
    def __init__(self):
        print("Init of B")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("Init of C")

    def feat(self):
        super().feature3()


# aObj = A()
obj = C()
obj.feat()
