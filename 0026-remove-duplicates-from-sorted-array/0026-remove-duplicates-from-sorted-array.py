# iterate through array
# whenever I see a new element increment k by 1 and set nums[k] to that elem. keep a var to store the cur unique elem

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur_elem = nums[0]
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != cur_elem:
                cur_elem = nums[i]
                nums[k] = cur_elem
                k += 1
        return k
        