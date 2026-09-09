# numbers = [3,4,6,2,7,2,8]

# target =10

# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             print(numbers[i], numbers[j])

numbers = [3,7,6,4,2,8,1,9]

target = 10

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])