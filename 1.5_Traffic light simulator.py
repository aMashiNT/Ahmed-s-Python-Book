# Traffic light simulator


color = input("Enter traffic light color (red, yellow, green): ").lower()

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color")
