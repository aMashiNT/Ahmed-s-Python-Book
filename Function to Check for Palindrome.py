#Function to Check for Palindrome

def is_palindrome(text):
    """Checks if a string is a palindrome."""
    # Convert to lowercase and remove spaces for accurate checking
    clean_text = "".join(char for char in text.lower() if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return clean_text == clean_text[::-1]

# Example usage
print(f"'racecar' is a palindrome: {is_palindrome('racecar')}")
# Output: 'racecar' is a palindrome: True
print(f"'Hello' is a palindrome: {is_palindrome('Hello')}")
# Output: 'Hello' is a palindrome: False
print(f"'A man a plan a canal Panama' is a palindrome: {is_palindrome('A man a plan a canal Panama')}")
# Output: 'A man a plan a canal Panama' is a palindrome: True