# numbers = [4, 7, 2, 7, 9, 2, 4, 1]

# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# largest = unique[0]

# for num in unique:
#     if num > largest:
#         largest = num

# print(largest)

# numbers = [1,2,3,4,5,20,4]

# unique =[]

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# largest = unique[0]

# for num in unique:
#     if num > largest:
#         largest = num

# print(largest)

# numbers = [1,2,3,4,90,47,28,484,484,23]

# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# largest = unique[0]

# for num in unique:
#     if num > largest:
#         largest = num

# print(largest)


numbers = [1,2,3,4,90,47,28,484,484,23]

largest = float('-inf')

for num in numbers:
    if numbers.count(num) == 1:
        if num > largest:
            largest = num

print (largest)
