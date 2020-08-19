def fibbo(n):
    a = 0
    b = 1
    if n == 0:
        print(a)

    else:
        if n < 0:
            print("Invalid number")

        else:
            print(a)
            print(b)

            for i in range(2, n):
                c = a + b
                a = b
                b = c
                print(c)


x = int(input("Enter no ele : "))

fibbo(x)
