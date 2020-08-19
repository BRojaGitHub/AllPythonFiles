from abc import ABC, abstractclassmethod


class Computer(ABC):
    @abstractclassmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("its running")


class WhiteBoard:
    def write(self):
        print("Writing here")


class Programmer:
    def work(self, pg):
        print("Solving bugs")
        print("Accessing abs method : ")
        pg.process()


# com = Computer()  Can't create obj of abstract class

lap = Laptop()
lap.process()

wht = WhiteBoard()
wht.write()

pgm = Programmer()
pgm.work(lap)
