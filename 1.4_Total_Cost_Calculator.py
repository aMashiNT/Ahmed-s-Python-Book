price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity
print("Total cost: ${:.2f}".format(total))
