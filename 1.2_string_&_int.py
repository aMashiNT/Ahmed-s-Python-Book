# string & int

phrase = input("Enter a word or phrase: ")
count = int(input("How many times to repeat? "))

# Repeat the phrase with spaces in between
output = (phrase + " ") * count
print(output.strip())  # strip() to remove trailing space

# Print the line below
print("=" * len(output.strip()))
