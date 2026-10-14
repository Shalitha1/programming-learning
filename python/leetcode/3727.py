
from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(num * num for num in nums)

        n = len(nums)
        positive_count = (n + 1) // 2

        score = sum(squares[n - positive_count:]) - sum(squares[:n - positive_count])

        return score


# nums = [1, 2, 3]

# solution = Solution()
# result = solution.maxAlternatingSum(nums)

# print("Input:", nums)
# print("Maximum alternating score:", result)
