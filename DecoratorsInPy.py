def div(a, b):
    print(a / b)


def decorator_for_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


div = decorator_for_div(div)
div(2, 4)

# new_div = decorator_for_div(div)
# new_div(2, 4)
