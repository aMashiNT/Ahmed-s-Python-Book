#Function with unknown number of parameters (*args)


def add_all(*numbers):
    total = sum(numbers)
    print("Sum of all numbers:", total)

add_all(1, 2, 3)
add_all(5, 10, 15, 20)
