class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


# class C(B):   # Multilevel Inheritance

class C(A, B):  # Multiple Inheritance
    def feature5(self):
        print("Feature 5 working")


aObj = A()
bObj = B()
cObj = C()

aObj.feature1()
aObj.feature2()

bObj.feature3()
bObj.feature4()

cObj.feature5()
