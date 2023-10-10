class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = list(sorted(nums))
        half = len(tmp[::2])
        nums[::2] = tmp[:half][::-1]
        nums[1::2] = tmp[half:][::-1]
        
            
        
        