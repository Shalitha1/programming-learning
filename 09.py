# numbers = [10,20,30,40]

# first_largest = float('-inf')
# second_largest = float('-inf')

# for num in numbers:
#     if num > first_largest:
#         second_largest = first_largest
#         first_largest = num
#     elif num > second_largest and num != first_largest:
#         second_largest = num

# print(second_largest)
# print(first_largest)
        
numbers = [1,2,3,1,4,5]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)
