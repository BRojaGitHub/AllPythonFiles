def sort(nums):
    for i in range(5):
        minpos = i  # min position
        for j in range(i, 6):
            if nums[j] < nums[minpos]:
                minpos = j

            temp = nums[i]
            nums[i] = nums[minpos]
            nums[minpos] = temp

            # print(nums)     # For checking og exact working


nums = [5, 3, 8, 6, 7, 2]
print("Before Sorting : ", nums)

sort(nums)

print("After Sorting : ", nums)
