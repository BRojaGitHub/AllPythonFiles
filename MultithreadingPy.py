from threading import *
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(3):
            print("Hello")
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(3):
            print("Hi")
            sleep(1)


t1 = Hello()  # Thread1 under main thread
t2 = Hi()  # Thread1 under main thread

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()

print("Bye")  # Executed by main thread
