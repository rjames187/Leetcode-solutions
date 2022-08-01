class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            hash_table[target - nums[i]] = i
        
        for j in range(len(nums)):
            if nums[j] in hash_table and hash_table[nums[j]] != j:
                return [hash_table[nums[j]], j]
                
            