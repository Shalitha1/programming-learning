numbers = [1,2,3,4]

# x = min(number)
# print(x)

smallest = numbers[0]

for num in numbers:
    if num > smallest:
        smallest = num

print(smallest)