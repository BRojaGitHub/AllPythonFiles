def add(a, b):
    c = a + b
    print(c)


add(5, 4)
add("Roja ", "B")
add(25.5, 25.5)


def person(name, age=18):  # Default
    print("Name: ", name)
    print("Age: ", age)


# Position
person("Roja", 24)

# Keyword
person(age=24, name="Roja")

# Default
person("Roja")

# Variable Length
print("Variable Length")


def sum(x, *y):
    print(x)
    print(y)
    z = x
    for i in y:
        z = z + i
    print("Sum: ", z)


sum(4, 5, 9, 1)


def addi(*y):
    print(y)
    z = 0
    print(z)
    for i in y:
        z = z + i
    print("Addition: ", z)


addi(4, 5, 9, 2)
