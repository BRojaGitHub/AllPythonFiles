print("# # # #")

print("# ", end="")
print("# ", end="")
print("# ", end="")
print("# ", end="")

print("")

for i in range(4):
    print("# ", end="")

print("")

for j in range(4):
    print("# ", end="")

print("")
print("Stop")

for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()

print("Stop")

for i in range(4):
    for j in range(i + 1):
        print("# ", end="")
    print()

print("Stop")

for i in range(4):
    for j in range(4 - i):
        print("# ", end="")
    print()
