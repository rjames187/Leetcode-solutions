from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        counts = c.most_common()
        num_evens = ceil(len(s) / 2)
        if counts[0][1] > num_evens:
            return ''
        
        res = [ None for i in range(len(s)) ]
        
        j = 0
        for letter, count in counts:
            for i in range(count):
                if j >= len(res):
                    j = 1
                res[j] = letter
                j += 2
        
        return ''.join(res)