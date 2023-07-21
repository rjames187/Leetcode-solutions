import math
from heapq import heappush, heappop

class Solution:
    def getDist(self, p):
        return math.sqrt((p[0] ** 2) + (p[1] ** 2))
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        h = []
        for p in points:
            dist = self.getDist(p)
            heappush(h, (dist, p))
        for i in range(k):
            res.append(heappop(h)[1])
        return res
        