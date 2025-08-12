#Greeting multiple people

def greet_people(*args):
    for name in args:
        print(f"Hello, {name}!")


greet_people("Ahmed", "Mashroor", "Coder")