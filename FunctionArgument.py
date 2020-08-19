print("ImMutable")


def update(x):
    print(id(x))

    x = 8
    print(id(x))

    print("Value of x: ", x)


a = 10
update(a)
print("Value of a: ", a)

update(10)

print(id(a))

print("Mutable")


def update(l):
    print(id(l))

    l[1] = 8
    print(id(l))

    print("Value of list: ", l)


l = [10, 20, 30]
print(id(l))
update(l)
print("List: ", l)
