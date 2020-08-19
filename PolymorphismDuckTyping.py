class PyCharm():
    def execute(self):
        print("Compiling")
        print("Running")


class MyCharm:
    def execute(self):
        print("Compiling")
        print("Convention Check")
        print("Spell Check")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()


# ide = PyCharm()
ide = MyCharm()
lp1 = Laptop()
lp1.code(ide)
