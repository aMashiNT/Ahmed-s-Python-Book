# animal guess game

animal  = "Lion"
animal1 = "Tiger"
animal2 = "Fox"
animal3 = "Buffalo"

guess  =  input("Can you guess an animal? ")

if guess.strip().lower() == animal.lower():
    print("You nailed it!")
else:
    print("Try again!")    

# Added strip function so if user types lower key still it will print "You nailed it!"