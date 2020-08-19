a = 5
b = 2

try:
    print("Resource Open")
    print(a / b)
    k = int(input("Enter a number: "))
    print(k)


except ZeroDivisionError as e:
    print("Hey, you can't divide a number by zero: ", e)

except ValueError as e:
    print("Invalid input: ", e)

except Exception as e:
    print("Something went wrong: ", e)


finally:
    print("Resource Closed")

print("Bye")
