temp = float(input("Enter temperature in Celsius: "))

if temp > 35:
    print("It's very hot!")
elif temp > 25:
    print("It's warm!")
elif temp > 15:
    print("It's pleasant!")
elif temp > 5:
    print("It's cold!")
else:
    print("It's freezing!")
