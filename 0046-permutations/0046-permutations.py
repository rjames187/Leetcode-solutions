class Solution:
    def backtrack(self, res, nums, perm, used):
        if len(perm) == len(nums):
            res.append(perm.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            perm.append(nums[i])
            used[i] = True
            self.backtrack(res, nums, perm, used)
            perm.pop()
            used[i] = False
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(res, nums, [], [False for i in range(len(nums))])
        return res
        