from functools import reduce

nums = [3, 2, 6, 8, 4, 6, 2, 9]
print("Nums: ", nums)


# 1. Filter

def is_even(n):
    return n % 2 == 0


# evens = list(filter(is_even, nums))

# Using Lambda in filter

evens = list(filter(lambda a: a % 2 == 0, nums))

odds = list(filter(lambda o: o % 2 != 0, nums))

print("Filter")
print(evens)
print(odds)

# 2. Map
# With true false condition

# doubles = list(map(lambda a: a % 2 == 0, nums))

# doubles = list(map(lambda a: a * 2, nums))

# Applying map on conditioned statement

doubles = list(map(lambda a: a * 2, evens))

print("Map")
print(doubles)


# 3. Reduce

# Import functools for Reduce method

def add_all(a, b):
    return a + b


# sums = reduce(add_all, nums)

sums = reduce(lambda a, b: a + b, nums)

print("Reduce")
print(sums)
