#   ** Reading from File **

rf = open("MyData", 'r')

# print(rf.read())

# print(rf.readline(), end="")  Prints 1st line
# print(rf.readline())  Prints 2nd line

# print(rf.readline(4))

#   ** Writing into File **

wf = open("WriteData", 'w')

# wf = open("WriteData", 'a')   Appends into file without erasing previous data

wf.write("This is write file \n")


for data in rf:     # For copying data from read to write file
    wf.write(data)


#   ** Image File **

im = open("Cattee.jpg", 'rb')
imo = open("MyCat.jpg", 'wb')
for i in im:
    imo.write(i)
