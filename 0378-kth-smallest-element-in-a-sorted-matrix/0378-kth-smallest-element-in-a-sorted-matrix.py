from heapq import heappush, heappop, heapify

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # initialize heap - O(K + K)
        h = []
        for r in range(len(matrix)):
            row = matrix[r]
            h.append((row[0], r, 1))
        heapify(h)
        
        # main algo - O(K Log N)
        for i in range(k - 1):
            val, r, c = heappop(h)
            if c < len(matrix):
                heappush(h, (matrix[r][c], r, c + 1))
        return heappop(h)[0]
            
        
        