numbers = [1,2,2,3,4,5,6,6,7]

result = []

seen = {}

for num in numbers:
    if num not in seen:
        result.append(num)
        seen[num] = True

print(result)