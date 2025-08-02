#Function to Find the Maximum of Two Numbers

def find_max(a, b):
    """Returns the larger of two numbers."""
    if a > b:
        return a
    else:
        return b

# Example usage
print(f"The maximum of 15 and 22 is: {find_max(15, 22)}")
# Output: The maximum of 15 and 22 is: 22