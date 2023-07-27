from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        h = [ (-val, key) for key, val in c.items() ]
        num_evens = ceil(len(s) / 2)
        heapify(h)
        if -h[0][0] > num_evens:
            return ''
        
        res = [ None for i in range(len(s)) ]
        
        j = 0
        while (h):
            count, letter = heappop(h)
            for i in range(-count):
                if j >= len(res):
                    j = 1
                res[j] = letter
                j += 2
        
        return ''.join(res)
        