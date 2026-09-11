# number = 12213

# original = number
# reversed_number = 0

# while number > 0:

#     digit = number % 10

#     reversed_number = reversed_number * 10 + digit

#     number = number // 10

# if original == reversed_number:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

number = 1234

original = number
reversed_number =0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number //10

if original == reversed_number:
    print("Palindrome")
else: print("Not palindrome")