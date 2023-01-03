class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        
        lst = sorted(list(hash_map.items()), key=lambda x: x[1], reverse=True)
        sliced = lst[slice(k)]
        
        return list(map(lambda x: x[0], sliced))