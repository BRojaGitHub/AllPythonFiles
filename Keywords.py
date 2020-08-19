def person(name, **data):
    print("Name : ", name)

    for i, j in data.items():
        print(i, j)


person("Roja", Age=24, City="Pune", PhNo=9730530328, Degree="BE")
