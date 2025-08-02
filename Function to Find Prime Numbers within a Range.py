# Function to Find Prime Numbers within a Range

def find_primes_in_range(start, end):
    """Finds all prime numbers between start and end (inclusive)."""
    prime_numbers = []
    for num in range(start, end + 1):
        if num > 1:  # Prime numbers are greater than 1
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
    return prime_numbers

# Example usage
prime_list = find_primes_in_range(10, 50)
print(f"Prime numbers between 10 and 50 are: {prime_list}")
# Output: Prime numbers between 10 and 50 are: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]