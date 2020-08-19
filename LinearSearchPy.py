pos = -1


def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1  # Same as : i = i + 1
    return False


list = [5, 8, 4, 6, 9, 2]
print("Linear Search List : ", list)
n = int(input("Enter value : "))

if search(list, n):
    print("Found at ", pos + 1, "th Location")
else:
    print("Not Found")
