class Solution:
    def getRange(self, a: int, b: int) -> str:
        if a == b:
            return str(a)
        return f'{a}->{b}'
    
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 1:
            return [str(nums[0])]
        if len(nums) == 0:
            return nums
        
        res = []
        cur_start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] + 1:
                res.append(self.getRange(cur_start, nums[i - 1]))
                cur_start = nums[i]
        res.append(self.getRange(cur_start, nums[len(nums) - 1]))
        return res
                