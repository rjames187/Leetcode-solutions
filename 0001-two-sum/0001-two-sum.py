class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, x in enumerate(nums):
            hash_table[x] = i
        
        for i, x in enumerate(nums):
            y = target - x
            if y in hash_table:
                j = hash_table[y]
                if i != j:
                    return [i, j]
# adding comment to test leethub to test dfsf