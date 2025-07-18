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

#The user has to use here capital letter "Lion" not "lion"
#Otherwise "Try again!" will show everytime!
# 
# Correct input = Lion, Tiger, Fox, Buffalo
# Wrong   input = lion, tiger, fox, buffalo 