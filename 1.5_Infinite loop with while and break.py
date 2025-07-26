# Infinite loop with while and break

while True:
    user = input("Type 'exit' to quit: ")
    if user.lower() == 'exit':
        break
    print("You typed:", user)
