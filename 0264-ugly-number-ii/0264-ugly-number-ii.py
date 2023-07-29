from heapq import heappush, heappop

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = [1]
        seen = set(h)
        for i in range(n - 1):
            num = heappop(h)
            for factor in [2, 3, 5]:
                new_num = num * factor
                if not new_num in seen:
                    heappush(h, new_num)
                    seen.add(new_num)
        return heappop(h)