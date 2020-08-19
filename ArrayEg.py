from array import *

arr = array('i', [])

n = int(input("Enter length of array: "))

for i in range(n):
    x = int(input("Enter next value: "))
    arr.append(x)

print(arr)

val = int(input("Enter value to search: "))

l = 0  # Counter variable
for d in arr:  # d is element in which every array variable is stored
    if d == val:  # d will be compared with entered value
        print(l)
        break
    l = +1

print(arr.index(val))

