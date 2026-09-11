numbers = [5, 3, 1, 3, 7, 5]

seen = []

for num in numbers:

    if num in seen:
        print(num)
        break

    seen.append(num)