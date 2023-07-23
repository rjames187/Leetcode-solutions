from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # python's heapq is a min heap but we need to pop the largest elems
        for i in range(len(nums)):
            nums[i] *= -1
        heapify(nums)
        for i in range(k - 1):
            heappop(nums)
        return heappop(nums) * -1
    
    # Time: O(k log(n) + n)
    # Space: O(1)
        