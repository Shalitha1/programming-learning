# def is_anagram(word1, word2):

#     if len(word1) != len(word2):
#         return False

#     frequency1 = {}
#     frequency2 = {}

#     for char in word1:
#         if char in frequency1:
#             frequency1[char] += 1
#         else:
#             frequency1[char] = 1

#     for char in word2:
#         if char in frequency2:
#             frequency2[char] += 1
#         else:
#             frequency2[char] = 1

#     return frequency1 == frequency2


# print(is_anagram("listen", "silent"))
# print(is_anagram("hello", "world"))

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    frequency1 = {}
    frequency2 = {}

    for char in word1:
        if char in frequency1:
            frequency1[char] += 1
        else:
            frequency1[char] = 1

    for char in word2:
        if char in frequency2:
            frequency2[char] += 1
        else:
            frequency2[char] = 1


    return frequency1 == frequency2

print(is_anagram("silent", "listen"))
