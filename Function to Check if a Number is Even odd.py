#Function to Check if a Number is Even or Odd

def check_even_odd(number):
    """Checks if a number is even or odd and returns the result as a string."""
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."

# Example usage
print(check_even_odd(7))
# Output: 7 is an odd number.
print(check_even_odd(12))
# Output: 12 is an even number.