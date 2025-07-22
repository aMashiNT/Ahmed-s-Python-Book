item1 = float(input("Enter the price of item 1: "))
item2 = float(input("Enter the price of item 2: "))
item3 = float(input("Enter the price of item 3: "))

total = item1 + item2 + item3
average = total / 3

print("Total cost is:", round(total, 2))
print("Average cost per item is:", round(average, 2))
