x = int(input("How many candies you want: "))
av = 5

i = 1
while i <= x:
    if i > av:
        print("Out of Stock")
        break

    print("Candy")
    i += 1

print("Bye")
