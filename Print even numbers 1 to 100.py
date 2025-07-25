# Print even numbers from 1 to 10 using continue

for i in range(1, 11):
    if i % 2 != 0:
        continue  # skip odd numbers
    print(i)
