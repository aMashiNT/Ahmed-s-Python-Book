#Sum Any Numbers

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum is:", total)

add_numbers(1, 2, 3)       # Sum is: 6
add_numbers(5, 10, 15, 20) # Sum is: 50
