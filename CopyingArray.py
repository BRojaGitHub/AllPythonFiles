from numpy import *

ar1 = array([1, 6, 4, 3])
ar2 = array([2, 4, 5, 7])

ar3 = ar1 + ar2

print(ar3)

print(ar1)
print(sin(ar1))
print(cos(ar1))
print(log(ar1))
print(sqrt(ar1))
print(min(ar1))
print(max(ar1))

print(concatenate([ar1, ar2]))

print("Stop")

print(ar1)
print(ar2)

print("Stop")

a = array([1, 5, 6, 4])
b = a.view()
a[1] = 7

print(a)
print(b)

print(id(a))
print(id(b))

print("Stop")

c = array([1, 5, 6, 4])
d = c.copy()
c[1] = 7

print(c)
print(d)

print(id(c))
print(id(d))