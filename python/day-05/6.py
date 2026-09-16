numbers = [1,3,4,5,6]

n = 6

actual_sum = 0

expected_sum = n * (n + 1) // 2

for num in numbers:
    actual_sum += num

missing = expected_sum - actual_sum

print(missing)