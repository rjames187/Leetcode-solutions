class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums) + 1):
            total += i
        for num in nums:
            total -= num
        return total
        