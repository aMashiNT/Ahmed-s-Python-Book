# Predefined animals
animals = ["lion", "tiger", "fox", "buffalo"]

# Get user input
guesses = input("Guess the animals (separate with spaces): ")

# Normalize input: lowercase + strip + split into list
guessed_list = guesses.lower().strip().split()

# Check guesses
for guess in guessed_list:
    if guess in animals:
        print(f"{guess.title()} is correct!")
    else:
        print(f"{guess.title()} is not in the list.")
