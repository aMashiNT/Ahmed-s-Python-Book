# Keyword Arguments

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Call by position:
describe_pet("dog", "Rex")

# Call by keyword:
describe_pet(pet_name="Whiskers", animal_type="cat")
