class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set_nums = set(nums)
        
        counts = {}
        
        for num in set_nums:
            counts[num] = nums.count(num)
        
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        return list(map(lambda x: x[0], sorted_counts[slice(k)]))