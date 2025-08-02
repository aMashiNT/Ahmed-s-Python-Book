#Function to Calculate Factorial

def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage
print(f"The factorial of 5 is: {factorial(5)}")
# Output: The factorial of 5 is: 120
print(f"The factorial of 0 is: {factorial(0)}")
# Output: The factorial of 0 is: 1