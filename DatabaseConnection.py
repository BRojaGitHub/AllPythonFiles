import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="roja", passwd="1234", database="roju")

myc = mydb.cursor()

# Cursor is like pointer pointing to the perticular location
# You can connect, execute, search & find data


print("** Available Databases **")
myc.execute("show databases")

for i in myc:  # All databases names
    print(i)

print("** Data from roju database **")

myc.execute("select * from Stud")

# for i in myc:  # All data from Stud
#   print(i)

print("Another way of fetching data")

# Fetching data from cursor and storing it somewhere
# here somewhere is "result"

result = myc.fetchall()

# result = myc.fetchone()

for i in result:  # All data from Stud
    print(i)
