nums = [5, 7, 8, 6, 3]

# print(nums[5])    Way 1

# for i in nums:    Way 2
# print(i)

it = iter(nums)  # Way 3
print(it.__next__())  # Way 3.1
print(it.__next__())

print(next(it))  # Way 3.2

for i in nums:  # Way 3.3
    print(i)


class TopTen:  # Way 4 (Creating own Iterator)
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


t = TopTen()
print(next(t))
for i in t:
    print(i)
