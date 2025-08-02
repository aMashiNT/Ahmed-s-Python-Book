# A Function with Multiple Parameters and a Return Value

def add_numbers(num1, num2):
    """This function takes two numbers and returns their sum."""
    sum_result = num1 + num2
    return sum_result

# Calling the function and storing the returned value
result = add_numbers(5, 10)
print(f"The sum is: {result}")

# Calling the function and using the returned value directly
print(f"The sum of 20 and 30 is: {add_numbers(20, 30)}")