text = "aabbcddeef"

frequency = {}

#count characters

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

#find first nin-repeating character

for char in text:
    if frequency[char] == 1:
        print(char)
        break