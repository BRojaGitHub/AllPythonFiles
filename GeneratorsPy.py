def topten():
    yield 1
    yield 2
    yield 3
    yield 4


def perfectsqr():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


val = topten()
per = perfectsqr()

print(val.__next__())
print(next(val))

for i in val:
    print(i)

print("Perfect Square from 1-10: ")
for i in per:
    print(i)
