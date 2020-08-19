def greet():
    print("Hello")
    print("Good Evening")


greet()


# Non returnable functions(Executes itself)
def add(x, y):
    z = x + y
    print("Add : ", z)


add(5, 4)


# Returnable functions
def add_sub(x, y):
    a = x * y
    return a


result = add_sub(5, 4)
print("Multiplication : ", result)


def plus_min(x, y):
    c = x + y
    d = x - y
    return c, d


r1, r2 = plus_min(5, 4)
print("Add : ", r1)
print("Sub : ", r2)
