class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # cases where all numbers are either negative or positive
        if nums[len(nums) - 1] < 0:
            return [num ** 2 for num in nums][::-1]
        if nums[0] >= 0:
            return [num ** 2 for num in nums]
        
        # case where we need to use two pointers
        res = []
        
        # initialize pointers
        left = 0
        while nums[left] < 0:
            left += 1
        left -= 1
        right = left + 1
        while right < len(nums) and nums[right] == 0:
            res.append(0)
            right += 1
        
        while left >= 0 or right < len(nums):
            if left < 0:
                res.append(nums[right] ** 2)
                right += 1
                continue
            if right >= len(nums):
                res.append(nums[left] ** 2)
                left -= 1
                continue
            if abs(nums[left]) > nums[right]:
                res.append(nums[right] ** 2)
                right += 1
            else:
                res.append(nums[left] ** 2)
                left -= 1
        
        return res
        
        
            
            
        
        
        