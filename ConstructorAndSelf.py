class Computer:
    # pass
    # We write "Pass" when we don't have idea about body of class

    def __init__(self):
        self.name = "Roja"
        self.age = 24

    def update(self):
        self.age = 25

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

c1.name = "Bugade"  # Changing the value of "name"

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

# c1.update()

print(c1.name)
print(c2.name)
print(c2.age)
