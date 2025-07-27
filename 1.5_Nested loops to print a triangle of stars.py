#  Nested loops to print a triangle of stars

for i in range(1, 9):        # Outer loop
    for j in range(i):       # Inner loop
        print("*", end="")
    print()                  # New line
