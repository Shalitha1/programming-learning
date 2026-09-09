# numbers = [1,2,3,3,3,4,5]

# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             print("Duplicated: ", numbers[i])

numbers = [1, 3, 4, 2, 2]

for i in range(len(numbers)):

    for j in range(i + 1, len(numbers)):

        if numbers[i] == numbers[j]:
            print("Duplicate:", numbers[i])