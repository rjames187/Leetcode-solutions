class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # generate right vals
        right = [0 for i in range(len(nums) - 1)] + [nums[len(nums) - 1]]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i] * right[i + 1]
        
        #generate left vals
        left = [nums[0]] + [0 for i in range(len(nums) - 1)]
        for i in range(1, len(nums)):
            left[i] = nums[i] * left[i - 1]
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(right[1])
            elif i == len(nums) - 1:
                res.append(left[len(nums) - 2])
            else:
                res.append(left[i - 1] * right[i + 1])
        
        return res
        
        