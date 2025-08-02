# A Function with Default Parameter Values

def describe_pet(animal_type, pet_name="unknown"):
    """Displays information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"Its name is {pet_name}.")

# Calling the function with all arguments
describe_pet("dog", "Buddy")

# Calling the function with only the required argument (using the default value for pet_name)
describe_pet("cat")