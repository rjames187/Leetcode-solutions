class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        counts = {}
        
        for num in nums:
            if num in counts:
                # check if already in res
                if counts[num] == -1:
                    continue
                counts[num] += 1
            else:
                counts[num] = 1
            # check if majority elem
            if counts[num] > n // 3:
                res.append(num)
                # mark as in res
                counts[num] = -1
        return res
            