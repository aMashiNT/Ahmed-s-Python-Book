# Check if a character is a vowel or consonant

ch = input("Enter a single letter: ").lower()

if ch in 'aeiou':
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not a letter")
