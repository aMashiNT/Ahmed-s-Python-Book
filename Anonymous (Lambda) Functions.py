#Anonymous (Lambda) Functions

# A one-line function to add two numbers
add = lambda x, y: x + y

print(add(5, 7))   # 12

# Use with sorted()
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
pairs_sorted = sorted(pairs, key=lambda item: item[1])
print(pairs_sorted)  # sorts by the word, not the number
