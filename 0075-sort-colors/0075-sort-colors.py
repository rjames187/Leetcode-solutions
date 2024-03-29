class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
        j = 0
        for i in range(0, 3):
            while counts[i] > 0:
                nums[j] = i
                j += 1
                counts[i] -= 1
        
                
        