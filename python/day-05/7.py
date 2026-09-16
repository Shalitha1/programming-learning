numbers = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(numbers)):

    current = numbers[i]
    needed = target - current

    if needed in seen:
        print([seen[needed], i])
        break

    seen[current] = i