a = 10
print(id(a))


def example():
    global a  # Globally overrides
    a = 15
    print(id(a))
    b = 17  # Local variable
    print("In function ", b)


example()
print("Outside Function ", a)

# Using Globals
print("Use of Globals")

a = 10
print(id(a))


def something():
    a = 9
    x = globals()['a']
    print(id(x))
    print("In function ", a)

    globals()['a'] = 15


something()
print("Outside Function ", a)
