#Function with multiple return values



def math_ops(a, b):
    return a + b, a - b, a * b

sum_, diff, product = math_ops(10, 5)
print("Sum:", sum_)
print("Difference:", diff)
print("Product:", product)
