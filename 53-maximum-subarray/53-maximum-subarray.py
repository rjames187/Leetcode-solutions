class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        dp = nums[0]
        for i in range(1, len(nums)):
            dp = max(nums[i], dp + nums[i])
            max_sum = max(dp, max_sum)
        return max_sum
            