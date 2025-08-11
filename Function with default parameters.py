#Function with default parameters
#Default values used if we don’t pass anything

def greet(name="Guest"):
    print("Hello,", name)

greet("Ahmed")  # Uses given name
greet()         # Uses default name
