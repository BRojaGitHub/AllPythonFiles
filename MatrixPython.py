from numpy import *

a1 = array([
    [1, 3, 4, 6, 8, 9],
    [8, 9, 7, 5, 2, 7]
])

a2 = array([8, 9, 7, 5, 2])

print(a1)
print(a2)

print(a1.dtype)
print(a1.ndim)
print(a1.shape)
print(a1.size)

a3 = a1.flatten()
print(a3)

a4 = a1.reshape(3, 4)
print(a4)

a4 = a1.reshape(2, 2, 3)
print(a4)

print("Matrices")

a5 = array([
    [1, 3, 4, 6],
    [8, 9, 7, 5]
])
m = matrix(a5)
print(m)

m = matrix('1,2,6,5 ; 7,8,9,6')
print(m)

m = matrix('0,2 ; 6,5 ; 7,8 ; 9,6')
print(m)

m = matrix('9,0,6 ; 5,7,8 ; 9,6,3')
print(m)

print("Diagonal")
print(diagonal(m))

print(m.min())
print(m.max())

m1 = matrix('9,1,6 ; 5,7,8 ; 9,6,3')
m2 = matrix('3,0,5 ; 4,5,6 ; 7,2,2')

m3 = m1 * m2
print(m3)
