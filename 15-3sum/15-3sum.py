class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = set()
        
        hash_table = {}
        for i, x in enumerate(nums):
            hash_table[x] = i
        
        hash_count = {}
        
        for k, z in enumerate(nums):
            if z in hash_count:
                hash_count[z] += 1
            else:
                hash_count[z] = 1
            
            if hash_count[z] < 3:
                for i, x in enumerate(nums):
                    y = 0 - x - z
                    if y in hash_table:
                        j = hash_table[y]
                        if i != j and k != j and k != i:
                            solution.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        
        return list(solution)