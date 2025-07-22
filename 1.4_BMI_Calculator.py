weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (meters): "))

bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))
