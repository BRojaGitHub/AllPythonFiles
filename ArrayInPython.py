from array import *

vals = array('i', [5, 9, -8, 4, 2])

print(vals.buffer_info())

print(vals.typecode)

vals.reverse()
print(vals)

print(vals[3])

for i in range(5):
    print("Array Values ", vals[i])

for i in range(len(vals)):
    print(vals[i])

print("Stop")

for e in vals:
    print(e)

val = array('u', ['a', 'e', 'i', 'o', 'u'])
for e in val:
    print(e)

print("Stop")

newArr = array(vals.typecode, (a for a in vals))
for e in newArr:
    print(e)

print("Stop")

newArr = array(vals.typecode, (a * a for a in vals))
for e in newArr:
    print(e)

print("Stop for While")

i = 0
while i < len(val):
    print(val[i])
    i += 1
