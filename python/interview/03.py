# numbers = [1, 2, 3, 4, 2, 5, 3, 6]

# seen = set()
# duplicates = set()

# for num in numbers:
#     if num in seen:
#         duplicates.add(num)
#     else:
#         seen.add(num)

# print(duplicates)

numbers = [1,2,3,3,4,5]

seen = set()
duplicated = set()

for i in numbers:
    if i in seen:
        duplicated.add(i)
    else:
        seen.add(i)