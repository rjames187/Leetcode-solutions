from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = Counter(s)
        for ch in t:
            if ch in counts:
                counts[ch] -= 1
                if counts[ch] == 0:
                    del counts[ch]
            else:
                return False
        
        return len(counts) == 0
        