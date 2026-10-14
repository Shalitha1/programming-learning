class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        num = [1,2,3]
        squares = []
        for num in nums:
            squares.append(num * nums)

        print(squares)