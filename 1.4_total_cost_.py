tax_rate = 0.08  # 8%
user_input = input("Please enter the price: ")
print("You typed:", user_input)  # Add this to debug
user = float(user_input)  # Use float for decimal inputs
total = user + (user * tax_rate)
print("Total cost: ${:.2f}".format(total))
