# numbers = [1,2,3,4,0,0,5,7,3,5,0,2]

# zeros =[]
# non_zeros = []

# for num in numbers:
#     if num == 0:
#         zeros.append(num)
#     else:
#         non_zeros.append(num)

# result = non_zeros + zeros

# print(result)

numbers = [0,0,0,1,1,1,1,]

zeros = []
non_zeros = []

for num in numbers:
    if num == 0:
        zeros.append(num)
    else:
        non_zeros.append(num)

result = non_zeros + zeros
print(result)
print(zeros)