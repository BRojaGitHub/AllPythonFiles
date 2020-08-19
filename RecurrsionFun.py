import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i = 0


def greet():
    global i
    i += 1  # Applying counter for checking how many times it prints
    print("Hello ", i)
    greet()


greet()
