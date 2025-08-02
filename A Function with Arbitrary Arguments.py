# A Function with Arbitrary Arguments (*args and **kwargs)

def print_all_arguments(*args, **kwargs):
    """This function prints all positional and keyword arguments passed to it."""
    print("Positional arguments:")
    for arg in args:
        print(f"- {arg}")

    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

# Calling the function with a mix of arguments
print_all_arguments(1, "hello", 3.14, name="Alice", age=30, city="New York")