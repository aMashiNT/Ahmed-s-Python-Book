# Using a function inside another

def multiply(a, b):
    return a * b

def double(num):
    return multiply(num, 2)

print(double(5))  # Output: 10
