# class PalindromeChecker:

#     def check(self, text):

#         left = 0
#         right = len(text) - 1

#         while left < right:

#             if text[left] != text[right]:
#                 return False

#             left += 1
#             right -= 1

#         return True


# obj = PalindromeChecker()

# result = obj.check("madam")

# if result:
#     print("Palindrome")
# else:
#     print("Not a palindrome") 

class PalindromeChecker:
    def check(self, text):
        left = 0
        right = len(text) - 1

        while left < right:
            if text[left] != text[right]:
                return False

            left +1
            right -1

            return True

obj = PalindromeChecker()

result = obj.check("lasal")

if result:
    print("palindrome")

else:
    print("not")
