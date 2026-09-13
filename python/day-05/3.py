text = "banana"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1


most_frequent = ""
highest_count = 0

for char in frequency:
    if frequency[char] > highest_count:
        highest_count = frequency[char]
        most_frequent = char

print(most_frequent)
