class A:
    def show(self):
        print("in A show")


class B(A):
    def show(self):
        print("in B show")


a = B()
a.show()
