text = input("Enter a text:")

vowels = "aeiou"
count = 0

for char in text.lower():
    if char in vowels:
        count += 1

print("vowel count:", count)